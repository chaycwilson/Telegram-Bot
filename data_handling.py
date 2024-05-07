import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_nutrition_info(food, quantity=1, unit=None):
    if unit:
        query = f"{quantity} {unit} of {food}"
    elif quantity is None and unit is None:
        query = food
    else: 
        query = f"{quantity} {food}"
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': os.environ.get('NUTRITIONIX_APP_ID'),
        'x-app-key': os.environ.get('NUTRITIONIX_API_KEY'),
    }
    response = requests.post(url, json={"query":query}, headers=headers)
    return response.json()

# def get

