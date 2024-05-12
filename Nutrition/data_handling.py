import requests
import os
from dotenv import load_dotenv
from Nutrition.formatting import extract_food_item
import telebot

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


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

def handle_calories(message):
    food, quantity, unit = extract_food_item(message.text)
    if not food:
        bot.reply_to(message, "I couldn't understand which food you're asking about. Please specify the food more clearly.")
        return

    try:
        quantity = float(quantity) if quantity else None
    except ValueError:
        quantity = None 
    try:
        nutrition_data = get_nutrition_info(food, quantity, unit)
        food_info = nutrition_data['foods'][0] if 'foods' in nutrition_data else None

        if food_info:
            if quantity and unit:
                calories = food_info.get('nf_calories', 'No data available')
                response = f"Calories in {quantity} {unit} of {food} is approximately {calories} kcal."
            else:
                calories = food_info.get('nf_calories', 'No data available')
                response = f"Estimated calories for a typical serving of {food} is about {calories} kcal. Please specify a quantity and unit for more accurate information."
        else:
            response = "Sorry, I couldn't find nutritional information for that item."
    except Exception as e:
        response = "Sorry, an error occurred while retrieving nutritional information."
        print(e)

    bot.reply_to(message, response)
    print("Response sent: ", response)

