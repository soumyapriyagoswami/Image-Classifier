"""
This module handles a capacity test for predicting images
"""
from __future__ import annotations

import os
#import time
#from multiprocessing import Process

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
        with open(image_path, 'rb') as f:
            response = self.client.post('/prediction', files={'file': f})
            assert response.status_code == 200
