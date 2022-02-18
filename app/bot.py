import telebot

from app.config import settings

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
print(bot.get_me())
