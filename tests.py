import pytest
import result.py
import "model creation.py"
import app.py
import cv

def preprocess_image_height():
    result = preprocess_image(img_path)
    assert result.shape[0] == 32
    
def preprocess_image_width():
    result = preprocess_image(img_path)
    assert result.shape[1] == 32

def preprocess_image_return_type():
    result = preprocess_image(img_path)
    assert type(result) is uint8
    
def result_return_type():
    result = result(img_path)
    assert type(result) is uint8

def dynamic_result_test():
    class_names = ["plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    image_path_dict = {
        "test_img/plane0" : class_names[0],
        "test_img/plane1" : class_names[0],
        "test_img/car0" : class_names[1],
        "test_img/car1" : class_names[1],
        "test_img/bird0" : class_names[2],
        "test_img/bird1" : class_names[2],
        "test_img/cat0" : class_names[3],
        "test_img/cat1" : class_names[3],
        "test_img/deer0" : class_names[4],
        "test_img/deer1" : class_names[4],
        "test_img/dog0" : class_names[5],
        "test_img/dog1" : class_names[5],
        "test_img/frog0" : class_names[6],
        "test_img/frog1" : class_names[6],
        "test_img/horse0" : class_names[7],
        "test_img/horse1" : class_names[7],
        "test_img/ship0" : class_names[8],
        "test_img/ship1" : class_names[8],
        "test_img/truck0" : class_names[9],
        "test_img/truck1" : class_names[9]
    }
    for (key, value in image_path_dict.items()):
        result = result(key)
        assert result == value
