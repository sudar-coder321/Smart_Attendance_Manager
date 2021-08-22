# Smart_Attendance_Manager
A python interactive and video generator and Excel Based attendance manager which authenticates/verifies user based on 1st his fingerprint and 2nd his voice

## Abstract
The System is based on two-stage authentication where voice is the first stage, and fingerprint the second stage. First the users speak in front of the audio input device and authenticate their voice after which they enter the classroom. A fingerprint sensor module would then be used to authenticate their fingerprint after which respective student’s attendance would be recorded. 

## Analysis of the Project 

### Voice Recgnitition Part

#### Registration

In voice training mode the user will be enrolled in the system. Here the input speech signal is captured by the sensor. Features such as speech pause, pitch, rate, frequency are extracted using the MFCC (Mel Frequency Cepstral Coefficients) feature extraction algorithm and a template will be generated (speaker modeling) based on the collection of scores obtained from the feature vectors and it will be stored in the database to be used in the future to recognize the user. 

#### Authentication

In Voice recognition mode verification of user takes place. Features such as speech pause, pitch, rate, frequency are extracted and score will be computed based on the extracted features and with the help of pattern matching module we will match the score with template stored in database and a decision is made whether the user is a valid user or not.

### Fingerprint Recognition System 

#### Registration

Image acquisition is done for both enrollment and verification processes. Images will be thinned using thinning process to make the features clear (to improve the accuracy). Next the features such as total number of ridges end points and Bifurcation points are extracted using Minutiae Feature extraction algorithm and template will be generated based on the collection of scores obtained from feature vectors and it will be stored in the database. 

#### Authentication

For verification of the user, after preprocessing, the features will be extracted and a score computed. With the help of pattern matching module, we will match the score with the template stored in the database and it will take a decision based on that.

## Algorithms used

### For Voice Recognition 

#### i) Feature Extraction from speech:-

##### Mel Frequency Cepstral Coefficient (MFCC):-  

##### Steps involved in MFCC 

 - Frame the signal into short frames. 

 - For each frame calculate the periodogram estimate of the power spectrum. 

 - Apply the mel filterbank to the power spectra, sum the energy in each filter. 

 - Take the logarithm of all filterbank energies. 

 - Take the DCT of the log filterbank energies. 

 - Keep DCT coefficients 2-13, discard the rest. 

#### (ii)Training the Model:- 

##### Hidden Markov Model (HMM): 
In an HMM, the system being modelled is assumed to be a Markov process with unknown parameters, and the challenge is to determine the hidden parameters from the observable parameters. A good HMM accurately models the real-world source of the observed real data and has the ability to simulate the source. 

##### Gaussian Mixture Model(GMM): 
A Gaussian mixture model is parameterized by two types of values, the mixture component weights and the component means and variances/covariances. 
For a Gaussian mixture model with K components, the kth component has a mean of  μk and variance of σk for the univariate case and a mean of (μ)⃗k and covariance matrix of Σk for the multivariate case 

##### Usage in application:-  
In our case we use GMMHMM model for training the model with N components and N mixtures and covariance type ‘diag’ i.e each component has a diagonal covariance matrix. 

#### (iii) For Converting speech to text:- 

##### Google Speech Recognition API 

Google Speech-to-Text Recognition module is a service that enables developers to convert audio to text by applying neural network models in an easy-to-use API.It has had a significant decrease in word error rate over the years with only 8% error rate (i.e) it is 92% accurate as of present stats.

### For Fingerprint Recognition

#### Scale-invariant feature transform:

##### Major advantages of SIFT are 

 - Locality: features are local, so robust to occlusion and clutter (no prior segmentation) 

 - Distinctiveness: individual features can be matched to a large database of objects 

 - Quantity: many features can be generated for even small objects 

 - Efficiency: close to real-time performance 

 - Extensibility: can easily be extended to a wide range of different feature types, with each adding robustness 

##### Steps involved in SIFT

 - Scale-space peak selection: Potential location for finding features. 

 - Keypoint Localization: Accurately locating the feature keypoints. 

 - Orientation Assignment: Assigning orientation to keypoints. 

 - Keypoint descriptor: Describing the keypoints as a high dimensional vector. 

 - Keypoint Matching: Image result for keypoint matching. Keypoints are the same thing as interest points. They are spatial locations, or points in the image that define what is interesting or what stand out in the image.

##  Proposed Block Diagram

### For Fingerprint Recognition System

![image](https://user-images.githubusercontent.com/60535124/130363340-f4727348-322e-4426-8aab-a90e7f94773e.png)

### For Voice Recognition System

![image](https://user-images.githubusercontent.com/60535124/130363358-36e8b2e5-ff42-4958-bf9a-e6b98fc38275.png)

### Proposed diagram for fusion system

![image](https://user-images.githubusercontent.com/60535124/130363374-b65cbde4-1dc1-48c5-b784-fe0122d4def1.png)

## Results for Fingerprint matching

### Finding Minutae Points

![image](https://user-images.githubusercontent.com/60535124/130363413-6f410a4b-44cc-46d0-9a80-e9b6dbd71ed3.png)

### Matching the Points

![image](https://user-images.githubusercontent.com/60535124/130363424-432111ae-f48e-42ec-bcb0-0e3a73701b1a.png)

### Calculating Score

![image](https://user-images.githubusercontent.com/60535124/130363431-c46c789e-5608-43eb-9148-4aa438d98f19.png)

## Results for Voice Recognition

### Voice Files 

![image](https://user-images.githubusercontent.com/60535124/130363555-0d023964-c245-4510-9c4b-64fe8a82c7e6.png)

### Generated Individual Models for each User (sudarshan Being a new user added after 1st execution)

![image](https://user-images.githubusercontent.com/60535124/130363576-72cc0b56-dc98-4619-9ad2-386552b0acbb.png)

### Generating Model and pkl file for a sample user(shruti)

![image](https://user-images.githubusercontent.com/60535124/130363627-1579a8ef-2da8-4890-872c-015bf5667ac4.png)

### Giving Attendance
![image](https://user-images.githubusercontent.com/60535124/130363500-845cf789-f353-4ae7-b02b-d6f5a9228740.png)


