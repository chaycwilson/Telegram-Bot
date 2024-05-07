import telebot
from data_handling import get_nutrition_info
from formatting import extract_food_item
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
print("Bot Token:", BOT_TOKEN)
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, welcome to the Nutri Bot!\nHow can i help you?")
    print(message)
    
@bot.message_handler(commands=["help"])
def send_help(message):
    for reply in replies:
        bot.reply_to(message, reply)
        
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
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


    
replies = [
    "Here are some things I can do...",
    "Use commands like /start or /hello to greet me.",
    "Ask me fitness and nutrional questions and I'll try my best to answer!"
]


if  __name__ == '__main__':
    bot.infinity_polling()
        




