import telebot
import random

bot = telebot.TeleBot("8644746757:AAG5nRC3yCdUGeWxl6D6tD0Z6l2Lb-e6OS4")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['generate_password'])
def generate_password(message):
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password_length = 12
    password = ""
    for _ in range(password_length):
        password += random.choice(symbols)
    bot.reply_to(message, f"Сгенерированный пароль: {password}")
    
bot.polling()
