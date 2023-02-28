import datetime
import json


# Модель заметки
class Note:
    def __init__(self, title, body, date=datetime.datetime.now(), id=None):
        self.title = title
        self.body = body
        self.date = date
        self.id = 1

    # Задание формата вывода
    def __str__(self):
        return f"{self.title}\t\t{self.date.strftime('%Y-%m-%d %H:%M')}\n\t{self.body}"

    def to_JSON(self):
        return json.dumps(f"{self.id};{self.title};{self.body};{self.date}")

    # Создание заметки по JSON строке
    @staticmethod
    def create_note(new_note):
        new_note: str = json.loads(new_note)
        list_ = new_note.split(';')
        return Note(list_[1], list_[2], datetime.datetime.strptime(list_[3], '%Y-%m-%d %H:%M:%S.%f'), int(list_[0]))

    # Определение сравнения по дате для сортировки
    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date
