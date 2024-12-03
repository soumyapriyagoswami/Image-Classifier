from __future__ import annotations

import os
import time
from multiprocessing import Process

from locust import HttpUser, between, task

from app import app

process = None

class WebsiteUser(HttpUser):
    @task
    def load_main(self):
        self.client.get("/")

    @task
    def predict_image_file(self):
        # Use a test image file
        if os.name == 'nt':  # for Windows
            image_path = r'.\test_images\0\Sign 0 (21).jpeg'
        else:  # for Linux
            image_path = './test_images/0/Sign 0 (21).jpeg'

        f = open(image_path, 'rb')

        files = {
            'file': ('the file', f, 'image/jpeg'),
        }

        # send a POST request to the prediction route with the test image file
        response = self.client.post('/prediction', files={'file': f})

        f.close()
