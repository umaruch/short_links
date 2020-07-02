from flask import jsonify, render_template, url_for, redirect, request, make_response

from shortlinks import app, config
from shortlinks import urls_services

@app.route('/')
def index():
    """Отправка в ответ главной страницы с которой и будет взаимодействовать пользователь"""
    return render_template(
        'index.html',
        version = config['version']
    )

@app.route('/new', methods = ['POST'])
def url_transform():
    """Функция возвращает клиенту укороченную ссылку"""
    if request.json and request.json.get('url', False):
        url = request.json.get('url')
        short_url = urls_services.create_short_url(url)
        return jsonify({'url':short_url})
    return make_response(jsonify({'status': 'error'}), 401)

@app.route('/<url>', methods = ['GET'])
def redirect_url(url):
    """Перенаправяет пользователя на нужный URL"""
    url = urls_services.short_to_full(url)
    if url:
        return redirect(url)
    
    return redirect(url_for('index'))

