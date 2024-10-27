"""Image Classification application trained on a CNN model that can be accessed from a browser"""

from flask import Flask, render_template, request
import os
import numpy as np
import cv2 as cv
from keras import models

app = Flask(__name__)

# Load the pre-trained model
model = models.load_model("image_classifier.h5")

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


def preprocess_image(img_path):
    """Adjusts the image to a standard format so that it can be read by the model"""
    img = cv.imread(img_path)
    img = cv.resize(img, (32, 32))
    img = img / 255.0
    img = img[None, :]
    return img


@app.route("/", methods=["GET", "POST"])
def index():
    """RESTful application that serves as a GUI for a user to check images to the trained model"""
    if request.method == "POST":
        # Handle the uploaded image
        file = request.files["file"]
        if file:
            # Save the uploaded image
            if not os.path.exists("static/uploads"):
                os.makedirs("static/uploads")
            img_path = "static/uploads/uploaded_image.png"
            file.save(img_path)

            # Preprocess the image
            img = preprocess_image(img_path)

            # Make a prediction
            prediction = model.predict(img)
            index = np.argmax(prediction)
            result = class_names[index]

            return render_template("index.html", result=result, image_path=img_path)

    return render_template("index.html", result=None, image_path=None)


if __name__ == "__main__":
    app.run(debug=True)
