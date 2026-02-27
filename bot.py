import telebot
import os
import random

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

players = []
current_question = None
current_answer = None

questions = [
    ("Кто выиграл ЧМ 2018?", "Франция"),
    ("Кто больше выиграл ЛЧ: Real Madrid или Barcelona?", "Real Madrid"),
    ("Кто из них португалец: Messi или Ronaldo?", "Ronaldo"),
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "⚽ Добро пожаловать в Miko Cup!\nНапиши /join чтобы участвовать")

@bot.message_handler(commands=['join'])
def join(message):
    if message.from_user.id not in players:
        players.append(message.from_user.id)
        bot.reply_to(message, "✅ Ты зарегистрирован!")
    else:
        bot.reply_to(message, "Ты уже в игре!")

@bot.message_handler(commands=['startcup'])
def startcup(message):
    global current_question, current_answer
    if len(players) < 2:
        bot.reply_to(message, "Нужно минимум 2 игрока!")
        return
    q = random.choice(questions)
