import telebot
import random
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

teams = [
    "Барселона",
    "Реал Мадрид"
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Нажми /game чтобы начать игру ⚽")

@bot.message_handler(commands=['game'])
def game(message):
    team1 = random.choice(teams)
    team2 = random.choice(teams)
    while team1 == team2:
        team2 = random.choice(teams)

    bot.send_message(message.chat.id, f"Кто победит?\n1️⃣ {team1}\n2️⃣ {team2}")

bot.infinity_polling()
