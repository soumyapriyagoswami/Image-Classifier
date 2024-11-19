"""This module handles the testing of the functionality of the system."""
import warnings
from result import result
from model_creation import model_creation
from app import preprocess_image, app
import pytest

IMAGE_TEST = "static/test_img/plane0.png"

#Gerkin Acceptance Test One
#
#Upload and Classify Image
#
#Given: A valid image file (e.g., JPEG, PNG).
#When: The user uploads the image.
#Then: The application should return a classification label within predefined categories.

def test_upload_and_classify_images():
    # Call the classify function and capture result
    result = result(IMAGE_TEST)

    # Assert that the result contains a classification label and confidence score
    assert "label" in result, "Expected result to contain a 'label' key"
    assert "confidence" in result, "Expected result to contain a 'confidence' key"
    assert isinstance(result["label"], str), "Label should be a string"
    assert isinstance(result["confidence"], float), "Confidence should be a float"
    assert 0.0 <= result["confidence"] <= 1.0, "Confidence score should be between 0 and 1"


#Gerkin Acceptance Test One
#
#Unsupported File Format
#
#Given: An unsupported file format (e.g., TXT, PDF).
#When: The user attempts to upload the file.
#Then: The application should prevent the upload and display an error message indicating the unsupported format.

def test_unsupported_file_format():    
    unsupported_file_path = "test_images/document.txt"

    # Call the classify function and expect an error
    with pytest.raises(ValueError, match="Unsupported file format"):
        result(unsupported_file_path)    