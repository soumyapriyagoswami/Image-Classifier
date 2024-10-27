"""
This module handles the prediction of the saved image and prints a string to console.
"""
import numpy as np
import cv2 as cv
from keras import datasets, models

def result(filename: str ="static/uploads/uploaded_image.png") -> str:
    """
    This function handles the grabbing of the preprocessed data and spits out a predictions.
    """
    # Load CIFAR-10 dataset
    (training_images,_training_labels),(testing_images,_testing_labels,)=datasets.cifar10.load_data()
    training_images, testing_images = training_images / 255, testing_images / 255
    # Class names for CIFAR-10
    class_names = ["plane","car","bird","cat","deer","dog","frog","horse","ship","truck"]
    # Load the pre-trained model
    model = models.load_model("image_classifier.h5")
    # Load and preprocess the image to make a prediction
    img = cv.imread(filename) # pylint: disable=no-member
    img = cv.resize(img, (32, 32))  # pylint: disable=no-member # Resize the image to match CIFAR-10 image size
    img = img / 255.00  # Normalize the pixel values to be between 0 and 1
    img = img[None, :]
    # Make a prediction
    return class_names[ np.argmax(model.predict(img))]
if __name__:
    print(f"Prediction is: {result(filename="static/uploads/uploaded_image.png")}")
