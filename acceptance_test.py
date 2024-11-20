"""This module handles the testing of the functionality of the system."""
import pytest
from result import result


IMAGE_TEST = "static/test_img/plane0.png"

#Gerkin Acceptance Test One
#
#Upload and Classify Image
#
#Given: A valid image file (e.g., JPEG, PNG).
#When: The user uploads the image.
#Then: The application should return a classification label within predefined categories.

def test_upload_and_classify_images():
    """This module handles the upload acceptance testing."""
    actual = result(IMAGE_TEST)

    class_names = ["plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    assert actual in class_names, f"Unexpected classification result: {actual}"


#Gerkin Acceptance Test One
#
#Unsupported File Format
#
#Given: An unsupported file format (e.g., TXT, PDF).
#When: The user attempts to upload the file.
#Then: The application should prevent the upload and
#display an error message indicating the unsupported format.

def test_unsupported_file_format():
    """This module handles the testing of file formats"""
    unsupported_file_path = "test_images/document.txt"

    # Call the classify function and expect an error
    with pytest.raises(ValueError, match="Unsupported file format"):
        result(unsupported_file_path)
