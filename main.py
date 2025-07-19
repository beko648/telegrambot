import telebot
import os
import openai
from keep_alive import keep_alive

BOT_TOKEN = os.environ["BOT_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

keep_alive()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men OpenAI bilan ishlaydigan Telegram botman!")

@bot.message_handler(func=lambda m: True)
def ai_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response['choices'][0]['message']['content'])
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {str(e)}")

bot.polling()
