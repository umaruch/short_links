import sqlite3
import os
import configparser

def connect_db(db_path:str):
    """"Функция возвращает объект подключения к БД"""

    #Проверка наличия файла
    #Если отсутствует то создаем внутри таблицу shorturls
    if not os.path.exists(db_path):
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE shorturls
            (
                full_url text,
                short_url text
            )
            """)
    else:
        connect = sqlite3.connect(db_path)

    return connect


def parse_config(config_path):
    """Функция парсит файл .config и возвращает словарь"""

    #Проверка наличия файла
    if not os.path.exists(config_path):
        default_config(config_path)

    config = configparser.ConfigParser()
    config.read(config_path)

    #Подобие преобразования строковых значений в логические
    if config.get("Settings", "csrf") == '1':
        csrf = True
    else:
        csrf = False

    if config.get("Settings", "debug") == '1':
        debug = True
    else:
        debug = False

    return {
        'version': config.get("Settings", "version"),
        'secret_key': config.get("Settings", "secret_key"),
        'database_path': config.get("Settings", "database_path"),
        'csrf': csrf,
        'debug': debug,
        'host': config.get("Settings", "host"),
        'port': int(config.get("Settings", "port"))
    }

def default_config(config_path):
    """На случай если пользователь своими кривыми руками удалит файл с настройками"""
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "version", "0.0.1")
    config.set("Settings", "secret_key", "mafoae3248234jvba3481bmbiuf")
    config.set("Settings", "database_path", "urls.db")
    config.set("Settings", "csrf", "1")
    config.set("Settings", "debug", "1")
    config.set("Settings", "host", "127.0.0.1")
    config.set("Settings", "port", "5000")
    
    with open(config_path, "w") as f:
        config.write(f)