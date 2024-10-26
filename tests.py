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
