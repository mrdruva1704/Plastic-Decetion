# BINTECH Project README

## Overview
BINTECH is a project designed to tackle the increasing plastic waste problem by implementing a robust plastic identification and recycling system. The system integrates various technologies including front-end development (HTML, CSS, JavaScript), back-end development (Python, Flask, OpenCV), machine learning (scikit-learn), and hardware components (Arduino board, LEDs).

The primary objective of BINTECH is to encourage individuals to deposit plastic waste into designated dustbins equipped with intelligent identification mechanisms. Upon depositing plastic waste, an image of the item is captured and processed using computer vision techniques. A machine learning algorithm, particularly the Convolutional Neural Network (CNN), is employed to classify the item as either plastic or non-plastic.

Feedback on the identification process is provided through LED lights. Upon successful identification, a QR code is generated. Users can scan this QR code using a mobile application, which converts it into recycling points for future use. Ultimately, BINTECH aims to promote environmental protection by incentivizing active participation in recycling efforts.

## Installation
To set up BINTECH on your system, follow these steps:

1. Clone the repository from GitHub:
   ```
   git clone https://github.com/yourusername/bintech.git
   ```

2. Navigate to the project directory:
   ```
   cd bintech
   ```

3. Install the required Python dependencies:
   ```
   pip install -r requirements.txt
   ``

4. Connect the hardware components (Arduino board, LEDs) according to the provided specifications.

5. Ensure all necessary software dependencies are installed on your machine.

## Usage
Follow these steps to utilize the BINTECH system:

1. Ensure the system is properly set up and all components are connected.

2. Start the Flask server:
   ```
   python app.py
   ```

3. Open the BINTECH web application in your browser and interact with the user interface to deposit plastic waste into the designated dustbins.

4. Upon depositing plastic waste, observe the LED feedback and wait for the identification process to complete.

5. Upon successful identification, a QR code will be generated. Use a mobile application to scan the QR code and convert it into recycling points.

## Contribution Guidelines
We welcome contributions to improve the BINTECH project. If you'd like to contribute, please follow these guidelines:

- Fork the repository and create a new branch for your feature or enhancement.
- Ensure your code adheres to the project's coding standards.
- Test your changes thoroughly before submitting a pull request.
- Provide detailed descriptions of your changes in the pull request
  
# Image Labelling using SVM

This script is used to label images in a given folder into two classes ('plastic' and 'not_plastic') using SVM. The labelled images can be used to train a model for object detection.

## Libraries Used

- os
- cv2
- numpy
- sklearn

## Dataset

The dataset is a folder containing images that are to be labelled. The dataset folder path is assigned to the `data_path` variable.

## Process

- Loop through the dataset folder and read the images
- Resize the images to 100x100
- Append the images and their labels to a list
- Convert the list to numpy arrays
- Split the dataset into training and testing sets
- Flatten the images and normalize the pixel values
- Train a Support Vector Machine (SVM) model using the training data
- Predict the labels of the testing set and calculate the accuracy
- Save the trained model using `joblib` for later use

## Predicting

- Load the saved SVM model
- Capture an image from the webcam
- Resize the image to 100x100
- Flatten the image and normalize the pixel values
- Pass the image through the model for prediction
- Draw a bounding box around the detected plastic bottle (if the prediction is 'plastic')
- Display the image and the predicted label

## Files

This script saves the trained SVM model as "PlasticDetection.pkl" and a test image with the predicted label as "test.jpg".

## Usage

1. Create a folder containing images that are to be labelled.
2. Set the folder path to `data_path`.
3. Run the script. It will label the images in the folder and save the trained model and a test image with the predicted label.
4. To use the trained model, load it using `joblib.load('PlasticDetection.pkl')` and pass an image through it for prediction.
