from shortlinks import config
from shortlinks.services import connect_db

class ShortUrl:
    """Класс через который будет удобно работать с таблицой в БД"""
    def __init__(self, full_url:str, short_url:str):
        self.full_url = full_url
        self.short_url = short_url    

    def save(self):
        """Сохранение обьекта в БД"""

        command = "INSERT INTO shorturls VALUES (?,?)"

        try:
            db = connect_db(config['database_path'])
            cursor = db.cursor()
            cursor.execute(command, (self.full_url, self.short_url))
            db.commit()
        except Exception as e:
        #Чуть позже заменить принты на логирование
            print(e)    

    @staticmethod
    def filter_by_short(link:str):
        """Поиск стандартной ссылки по короткой"""

        command = "SELECT * FROM shorturls WHERE short_url=?"

        try:
            db = connect_db(config['database_path'])
            cursor = db.cursor()
            obj = cursor.execute(command, [link]).fetchall()
            #Проверка на наличие значений из таблицы    
            if not obj == []:
                return ShortUrl(obj[0][0], obj[0][1])
            else:
                return None

        except Exception as e:
        #Чуть позже заменить принты на логирование
            print(e)  

    @staticmethod
    def filter_by_long(link:str):
        """Поиск короткой ссылки по стандартной"""

        command = "SELECT * FROM shorturls WHERE full_url=?"

        try:
            db = connect_db(config['database_path'])
            cursor = db.cursor()
            obj = cursor.execute(command, [link]).fetchall()

            #Проверка на наличие значений из таблицы
            if not obj == []:
                return ShortUrl(obj[0][0], obj[0][1])
            else:
                return None
        
        except Exception as e:
            #Чуть позже заменить принты на логирование
            print(e)    
     
