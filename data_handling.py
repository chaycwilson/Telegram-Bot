import requests

NUTRITIONIX_APP_ID = '76e8ceb8'
NUTRITIONIX_API_KEY = '3e632828fb8442581238313daebd2ea2'

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
        'x-app-id': NUTRITIONIX_APP_ID,
        'x-app-key': NUTRITIONIX_API_KEY,
    }
    response = requests.post(url, json={"query":query}, headers=headers)
    return response.json()

# def get

