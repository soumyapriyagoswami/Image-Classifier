"""
This module handles a capacity test for predicting images
"""
from __future__ import annotations

from locust import HttpUser, task #, between
#from app import app

PROCESS = None

IMAGE_TEST = "static/test_img/plane0.png"

class WebsiteUser(HttpUser):
    """This test class handles simulates one user"""
    @task
    def load_main(self):
        """This function handles getting the index page"""
        self.client.get("/")

    @task
    def predict_image_file(self):
        """This function handles uploading an image"""
        # send a POST request to the prediction route with the test image file
        response = self.client.get("/")
        print(response)
        csrf_token = (
            response.data.decode().split('name="csrf_token" value="')[1].split('"')[0])

        with open(IMAGE_TEST, "rb") as img_file:
            data = {"file": (img_file, "plane0.png"),
                "csrf_token": csrf_token}
            response = self.client.post("/", data=data, content_type="multipart/form-data")
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

        assert b"Result:" in response.data  # Verifying "Result:" is in the HTML response
        #assert result() in ["plane", "train"]
