import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000/chatbot/api"

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get_main_categories(self):
        response = requests.get(f"{self.base_url}/main-categories/")
        return response.json() if response.status_code == 200 else []

    def get_sub_categories(self, main_category_id):
        response = requests.get(f"{self.base_url}/main-categories/{main_category_id}/sub-categories/")
        return response.json() if response.status_code == 200 else []

    def get_recommended_products(self, sub_category_id, condition, product_name=None):
        data = {"condition": condition}
        if product_name:
            data["product_name"] = product_name

        response = requests.post(f"{self.base_url}/sub-categories/{sub_category_id}/recommend-products/", data=data)
        return response.json() if response.status_code == 200 else {"products": []}

    def get_aspect_ratio(self, product_id):
        response = requests.get(f"{self.base_url}/products/{product_id}/aspect-ratio/")
        return response.json() if response.status_code == 200 else []
