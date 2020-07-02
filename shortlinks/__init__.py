import flask
import os

from shortlinks.services import parse_config

config = parse_config(".config")

"""Инициализация приложения"""
app = flask.Flask(__name__)
from shortlinks import views
app.config.update(
    SECRET_KEY = config['secret_key'],
    CSRF_ENABLED = config['csrf'],
    DEBUG = config['debug'],
    HOST = config['host'],
    PORT = config['port']
)

""" Загрузка иконки сайта,
    В ходе тяжелой умственной активности было решено перенести эту функцию сюда
    так как она не особо смотрелась на фоне действительно полезных функция во views
"""
@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
