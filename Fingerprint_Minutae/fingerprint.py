import cv2 as cv
from glob import glob
import os
import sys
import numpy as np
from utils import singularity
from utils.segmentation import create_segmented_and_variance_images
from utils.normalization import normalize
from utils.gabor_filter import gabor_filter
from utils.frequency import ridge_freq
from utils import orientation
from utils.crossing_numbers import calculate_minutiaes
from tqdm import tqdm
from utils.skeletonize import skeletonize

os.chdir("F:\Fingerprint_Minutae")

def fingerprint(input_img):
    block_size = 16

    # pipe line picture re https://www.cse.iitk.ac.in/users/biometrics/pages/111.JPG
    # normalization -> orientation -> frequency -> mask -> filtering

    # normalization - removes the effects of sensor noise and finger pressure differences.
    normalized_img = normalize(input_img.copy(), float(100), float(100))

    # color threshold
    # threshold_img = normalized_img
    # _, threshold_im = cv.threshold(normalized_img,127,255,cv.THRESH_OTSU)
    # cv.imshow('color_threshold', normalized_img); cv.waitKeyEx()

    # ROI and normalisation
    (segmented_img, normim, mask) = create_segmented_and_variance_images(normalized_img, block_size, 0.2)

    # orientations
    angles = orientation.calculate_angles(normalized_img, W=block_size, smoth=False)
    orientation_img = orientation.visualize_angles(segmented_img, mask, angles, W=block_size)

    # find the overall frequency of ridges in Wavelet Domain
    freq = ridge_freq(normim, mask, angles, block_size, kernel_size=5, minWaveLength=5, maxWaveLength=15)

    # create gabor filter and do the actual filtering
    gabor_img = gabor_filter(normim, angles, freq)

    # thinning oor skeletonize
    thin_image = skeletonize(gabor_img)

    # minutias
    minutias, minutias_keypoints = calculate_minutiaes(thin_image)

    # singularities
    singularities_img,  singularities_keypoints = singularity.calculate_singularities(thin_image, angles, 1, block_size, mask)

    # visualize pipeline stage by stage
    return [minutias, minutias_keypoints, singularities_img, singularities_keypoints]


if __name__ == '__main__':
    image_name = sys.argv[1]
    img1 = cv.imread(image_name, cv.IMREAD_GRAYSCALE)
    cv.imshow('Original',img1)
    Testimg_results = fingerprint(img1)
    orb = cv.ORB_create()
    # Compute descriptors
    _, des_test = orb.compute(img1, Testimg_results[1])

    # open images
    img_dir = './Database/*'
    output_dir = './Processedimages/'
    def open_images(directory):
        images_paths = glob(directory)
        return np.array([cv.imread(img_path,0) for img_path in images_paths])

    images = open_images(img_dir)

    os.makedirs(output_dir, exist_ok=True)
    for i, img in enumerate(images):
        results = fingerprint(img)
        result = np.concatenate(results[:3:2], 1).astype(np.uint8)
        cv.imwrite(output_dir+str(i)+'.png', result)
        orb = cv.ORB_create()
        # Compute descriptors
        _, des = orb.compute(img, results[1])
        bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
        matches = sorted(bf.match(des_test, des), key= lambda match:match.distance)
        score = 0
        for match in matches:
            score += match.distance
        score_threshold = 20
        if score/len(matches) < score_threshold:
            print("Fingerprint matches.",score/len(matches))
            cv.imshow('Matched Img', img)
            cv.waitKey()
        else:
            print(score/len(matches))
