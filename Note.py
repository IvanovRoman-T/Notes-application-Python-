import datetime
import json


# Модель заметки
class Note:

    def __init__(self, title, body, date=datetime.datetime.now(), id=None):
        self.__title = title
        self.__body = body
        self.__date = date
        if id is None:
            self.__id = date.microsecond
        else:
            self.__id = id

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def get_date(self):
        return self.__date

    def set_title(self, value):
        self.__title = value

    def set_body(self, value):
        self.__body = value

    # Задание формата вывода
    def __str__(self):
        return f"{self.__title}\t\t{self.__date.strftime('%Y-%m-%d %H:%M')}\n\t{self.__body}"

    def to_json(self):
        return json.dumps(f"{self.__id};{self.__title};{self.__body};{self.__date}")

    # Определение сравнения по дате для сортировки
    def __le__(self, other):
        return self.__date <= other.__date

    def __ge__(self, other):
        return self.__date >= other.__date
