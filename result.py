import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, models

def result(filename: str ="static/uploads/uploaded_image.png"):
    # Load CIFAR-10 dataset
    (training_images, training_labels), (
        testing_images,
        testing_labels,
    ) = datasets.cifar10.load_data()
    training_images, testing_images = training_images / 255, testing_images / 255
    
    # Class names for CIFAR-10
    class_names = [
        "plane",
        "car",
        "bird",
        "cat",
        "deer",
        "dog",
        "frog",
        "horse",
        "ship",
        "truck",
    ]
    
    # Display some sample images from the dataset
    for i in range(16):
        plt.subplot(4, 4, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(training_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[training_labels[i][0]])
    plt.show()
    
    # Constructing neural net
    
    
    # Load the pre-trained model
    
    model = models.load_model("image_classifier.h5")
    
    # Load and preprocess the image to make a prediction
    
    img = cv.imread(filename)
    
    img = cv.resize(img, (32, 32))  # Resize the image to match CIFAR-10 image size
    img = img / 255.00  # Normalize the pixel values to be between 0 and 1
    img = img[None, :]
    
    # Make a prediction
    prediction = model.predict(img)
    return class_names[ np.argmax(prediction)]

if __name__ == "__main_":
    print(f"Prediction is: {result(filename="static/uploads/uploaded_image.png")}")
