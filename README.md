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
