import pytest
from result import result
from app import preprocess_image
import cv

def preprocess_image_height():
    result = preprocess_image("test_img/plane0.png")
    assert result.shape[0] == 32
    
def preprocess_image_width():
    result = preprocess_image("test_img/plane0.png")
    assert result.shape[1] == 32

def preprocess_image_return_type():
    result = preprocess_image("test_img/plane0.png")
    assert type(result) is uint8
    
def result_return_type():
    result = result("test_img/plane0")
    assert type(result) is uint8

def dynamic_result_test():
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
        result = result(key)
        assert result == value
