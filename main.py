import telebot
from data_handling import handle_calories
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

@bot.message_handler(commands=["fitness"]) 
def get_fitness(message):
    # Get user input from message text
    if message:
        bot.reply_to(message, "Tell me about your goals and ill suggest some exercises")
        
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    handle_calories(message)
    # print("Response sent: ", response)


replies = [
    "Here are some things I can do...",
    "Use commands like /start or /hello to greet me.",
    "Use /fitness to give your goals and ill suggest some exercises!",
    "Ask me fitness and nutrional questions and I'll try my best to answer!"
]


if  __name__ == '__main__':
    bot.infinity_polling()
        




