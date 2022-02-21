from telebot.apihelper import ApiTelegramException

from app.bot import bot
from app.invites import GitHub
from app.validator import is_valid_email
from app.config import settings

github = GitHub()


def is_subscribed(chat_id, user_id):
    try:
        bot.get_chat_member(chat_id, user_id)
        return True
    except ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: user not found':
            return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}.')
        bot.send_message(message.chat.id, f'Enter your email, I will share invitation for you.')


@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.chat.type != "private":
        return

    if is_subscribed(chat_id=settings.TG_CHAT_ID, user_id=message.chat.id):
        email = message.text
        if is_valid_email(email):
            github.create_invite(email)
        else:
            bot.send_message(message.chat.id, f'Email is not valid. Check it, and try again.')
    else:
        bot.send_message(message.chat.id, f'Please write to @jscursed to join us.')


@bot.message_handler(content_types=["new_chat_members"])
def send_hello(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}.')
    bot.send_message(message.chat.id, f'Enter your email, I will share invitation for you.')
