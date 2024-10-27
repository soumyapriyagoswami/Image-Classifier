"""This module handles the testing of the functionality of the system."""
import numpy as np
import pytest
from result import result
from app import preprocess_image

def preprocess_image_height():
    """This test case handles loading an image, checking if the new height is equal"""
    assert preprocess_image("test_img/plane0.png").shape[0] == 32

def preprocess_image_width():
    """This test case handles loading an image and checking if the new width is equal to the expected value."""
    assert preprocess_image("test_img/plane0.png").shape[1] == 32

def preprocess_image_return_type():
    """This test case handles loading an image and checking the return type."""
    assert isinstance(preprocess_image("test_img/plane0.png"), np.uint8)

def result_return_type():
    """This test case handles entire functionality of result and checks the return type"""
    assert isinstance(result("test_img/plane0"), np.uint8)

def dynamic_result_test():
    """This test case is a dynamic test, testing two of each image to ensure the model is trained and predicting correctly"""
    class_names = ["plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    image_path_dict = {
        "test_img/plane0.png" : class_names[0],
        "test_img/plane1.png" : class_names[0],
        "test_img/car0.png" : class_names[1],
        "test_img/car1.png" : class_names[1],
        "test_img/bird0.png" : class_names[2],
        "test_img/bird1.png" : class_names[2],
        "test_img/cat0.png" : class_names[3],
        "test_img/cat1.png" : class_names[3],
        "test_img/deer0.png" : class_names[4],
        "test_img/deer1.png" : class_names[4],
        "test_img/dog0.png" : class_names[5],
        "test_img/dog1.png" : class_names[5],
        "test_img/frog0.png" : class_names[6],
        "test_img/frog1.png" : class_names[6],
        "test_img/horse0.png" : class_names[7],
        "test_img/horse1.png" : class_names[7],
        "test_img/ship0.png" : class_names[8],
        "test_img/ship1.png" : class_names[8],
        "test_img/truck0.png" : class_names[9],
        "test_img/truck1.png" : class_names[9]
    }
    for key, value in image_path_dict.items():
        assert result(key) == value
