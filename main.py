import telebot
from Nutrition.data_handling import handle_calories
from Fitness.fitness import fetch_exercises_by_target, format_exercise_data, get_metrics
import os
from dotenv import load_dotenv

load_dotenv()
user_data = {}

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, welcome to the Nutri Bot!\nHow can I help you?")
    print(message)

@bot.message_handler(commands=["help"])
def send_help(message):
    replies = [
        "Here are some things I can do...",
        "Use commands like /start or /hello to greet me.",
        "Use /calories and I will give you the number of calories in your favorite food!",
        "Use /fitness to give your goals and I'll suggest some exercises!"]
    for reply in replies:
        bot.reply_to(message, reply)

@bot.message_handler(commands=["fitness"])
def start_fitness(message):
    msg = bot.send_message(message.chat.id, "Welcome! What's your height in cm?")
    bot.register_next_step_handler(msg, process_height_step)

#Go through all the functions to fulfill the metrics parameters
def process_height_step(message):
    try:
        height = int(message.text)
        user_data['height'] = height
        msg = bot.send_message(message.chat.id, "What's your weight in kg?")
        bot.register_next_step_handler(msg, process_weight_step)
    except ValueError:
        msg = bot.send_message(message.chat.id, "Please enter a valid number for height.")
        bot.register_next_step_handler(msg, process_height_step)

def process_weight_step(message):
    try:
        weight = int(message.text)
        user_data['weight'] = weight
        msg = bot.send_message(message.chat.id, "Which body part would you like to target? (e.g., abs, quads, pectorals)")
        bot.register_next_step_handler(msg, process_body_part_step)
    except ValueError:
        msg = bot.send_message(message.chat.id, "Please enter a valid number for weight.")
        bot.register_next_step_handler(msg, process_weight_step)

def process_body_part_step(message):
    body_part = message.text.lower()
    user_data['body_part'] = body_part
    metrics = get_metrics(user_data['height'], user_data['weight'])
    exercises = fetch_exercises_by_target(body_part)
    
    bmi_response = f"Your BMI is {metrics['bmi']:.2f}.\n\nHere are some exercises you can do to target your {body_part}:"
    bot.send_message(message.chat.id, bmi_response, parse_mode="Markdown")
    #If there are exercises loop through them and format it as such
    if exercises:
        for exercise in exercises:
            exercise_detail = f"• **Name**: {exercise['name']} \n  - **Equipment**: {exercise['equipment']} \n  - **Target**: {exercise['target']}"
            bot.send_animation(message.chat.id, exercise['gifUrl'], caption=exercise_detail, parse_mode="Markdown")
    else:
        no_exercises_response = "No exercises found for the selected body part."
        bot.send_message(message.chat.id, no_exercises_response, parse_mode="Markdown")



@bot.message_handler(commands=["calories"])
def request_calories(message):
    msg = bot.reply_to(message, "Please enter the food item with its weight (e.g., How many calories in 100g of chicken?).")
    bot.register_next_step_handler(msg, handle_calories)

if __name__ == '__main__':
    print("Running")
    bot.infinity_polling()
