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
