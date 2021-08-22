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
