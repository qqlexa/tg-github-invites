import os

from telebot import types
import flask

from app.bot_handlers import bot
from app.config import settings

server = flask.Flask(__name__)


@server.route('/' + settings.TELEGRAM_TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates(
        [types.Update.de_json(flask.request.stream.read().decode('utf-8'))]
    )
    return '!', 200


@server.route('/', methods=['GET'])
def index():
    bot.remove_webhook()
    bot.set_webhook(
        url='https://{}.herokuapp.com/{}'.format(settings.APP_NAME, settings.TELEGRAM_TOKEN)
    )
    return 'Hello from Heroku!', 200


if __name__ == '__main__':
    # https://momentum-bots.top/blog/2018/05/24/botheroku/
    # bot.remove_webhook()
    # server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    bot.polling(none_stop=True)  # use to local run
