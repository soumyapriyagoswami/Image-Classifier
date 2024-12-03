"""
This module handles a capacity test for predicting images
"""
from __future__ import annotations

import os
import time
from multiprocessing import Process

from locust import HttpUser, between, task

from app import app

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
        # Use a test image file
        if os.name == 'nt':  # for Windows
            image_path = IMAGE_TEST
        else:  # for Linux
            image_path = IMAGE_TEST

        f = open(image_path, 'rb')

        files = {
            'file': ('the file', f, 'image/jpeg'),
        }

        # send a POST request to the prediction route with the test image file
        response = self.client.post('/prediction', files={'file': f})

        f.close()
