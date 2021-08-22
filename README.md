# Smart_Attendance_Manager
A python interactive and video generator and Excel Based attendance manager which authenticates/verifies user based on 1st his fingerprint and 2nd his voice

## Abstract
We plan to have a two-stage authentication where voice is the first stage, and fingerprint the second stage. First the users will would have to speak in front of the audio input device and authenticate their voice after which they can enter the classroom. A fingerprint sensor module would then be used to authenticate their fingerprint and after their fingerprint is successfully verified, the respective student’s attendance would be recorded. 

## Analysis of the Project 

### Voice Recgnitition Part

#### Registration

In voice training mode the user will be enrolled in the system. Here the input speech signal is captured by the sensor. The captured voice would not be accurate due to the environmental conditions and other background noises.So first we will do signal degradation and other preprocessing techniques to remove the unwanted noise and improve the signal quality.Then the features such as speech pause, pitch, rate, frequency are extracted using the MFCC (Mel Frequency Cepstral Coefficients) feature extraction algorithm and a template will be generated (speaker modeling) based on the collection of scores obtained from the feature vectors and it will be stored in the database to be used in the future to recognize the user. 

#### Authentication

In Voice recognition mode verification of user takes place. Here too the input signals are preprocessed to improve the signal quality. Then the features such as speech pause, pitch, rate, frequency are extracted and score will be computed based on the extracted features and with the help of pattern matching module we will match the score with template stored in database and a decision is made whether the user is a valid user or not.

### Fingerprint Recognition System 

#### Registration

Image acquisition is done for both enrollment and verification processes. The fingerprint is captured as an input by the device by placing the finger at various angles to capture all the features.Next step is preprocessing using Binarization to make ridges and fudges in black and white respectively which makes it easier for the computer to recognize. Then these images will be thinned using thinning process to make the features clear (to improve the accuracy). Next the features such as total number of ridges end points and Bifurcation points are extracted using Minutiae Feature extraction algorithm and template will be generated based on the collection of scores obtained from feature vectors and it will be stored in the database. 

#### Authentication

For verification of the user, after preprocessing, the features will be extracted and a score computed. With the help of pattern matching module, we will match the score with the template stored in the database and it will take a decision based on that.

### Combined System 

#### Enrollment Phase

In first stage the Voice signal will be captured by the sensor. Signal degradation is done and multiple features (pitch, rate, frequency) will be extracted and it will be fused together to get feature fusion. After that template is generated based on the scores obtained from the features and it will be stored in the database.In second stage Fingerprint images are extracted as a dataset and fed into the system. Preprocessing is done, multiple features (total number of ridges end point and bifurcation points) will be extracted, and it will be used to generate a set of values known as scores. After that, a template is generated based on the scores obtained from the features and it will be stored in the database.

#### Verification Phase

In first stage the Voice signal will be captured by the sensor. Signal degradation is done and multiple features (pitch, rate, frequency) will be extracted and it will be fused together to get feature fusion. After that scores will be generated based on the fusion vectors.Preprocessing is done and multiple features (total number of ridges end point and bifurcation points) will be extracted as feature vectors and these vectors would be fused together using a mathematical function to generate a score.These generated scores are sent to the pattern matching module which matches these scores with the template stored in the database and it will take a decision based on that.

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
