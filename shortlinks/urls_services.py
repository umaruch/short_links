import string
import random
from shortlinks import model

""""Символы, используемые при генерации короткого url"""
URL_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits

def generate_url():
    url = ""
    for i in range(6):
        url += random.choice(URL_CHARS)
    return url

def create_short_url(full_url):
    """Создает короткую строку"""
    #Проверка наличия данного исходного URL в базе данных, дабы не создавать то-же самое заного
    url = model.ShortUrl.filter_by_long(full_url)
    if url:
        return url.short_url
    
    #Если не было совпадения генерируем новый короткий URl пока не выпадет оригинальный
    while True:
        short_url = generate_url()
        url = model.ShortUrl.filter_by_short(short_url)
        if not url:
            model.ShortUrl(full_url, short_url).save()
            return short_url   


def short_to_full(short_url):
    url = model.ShortUrl.filter_by_short(short_url)
    if url:
        return url.full_url
    
    return None
    