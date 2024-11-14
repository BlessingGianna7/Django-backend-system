from django.conf import settings
import requests
class APIHandler:
    BASE_URL = "http://localhost:8000"  # This will connect to your FastAPI server

    @staticmethod
    def get(endpoint):
        response = requests.get(f"{APIHandler.BASE_URL}{endpoint}")
        return response.json()

    @staticmethod
    def post(endpoint, data):
        response = requests.post(f"{APIHandler.BASE_URL}{endpoint}", json=data)
        return response.json()

    @staticmethod
    def put(endpoint, data):
        response = requests.put(f"{APIHandler.BASE_URL}{endpoint}", json=data)
        return response.json()

    @staticmethod
    def delete(endpoint):
        response = requests.delete(f"{APIHandler.BASE_URL}{endpoint}")
        return response.json()