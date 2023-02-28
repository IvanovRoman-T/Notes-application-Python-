from Notebook import Notebook
from datetime import datetime as dt
from FileManager import FileManager


class UI:
    notebook = None
    flag = True

    def __init__(self):
        self.notebook = Notebook()

    def start(self):
        FileManager.read("notes.json", self.notebook)
        self.help()
        while self.flag:
            self.command()

    def command(self):
        com = input("Введите комманду: ")
        if com is 'help':
            self.help()
        elif com is '1':
            self.show()
        elif com is '2':
            self.add()
        elif com is '3':
            self.delete()
        elif com is '4':
            self.edit()
        elif com is '5':
            self.save()
        elif com is '0':
            self.exit()
        else:
            print("Неопознанная комманда")

    def help(self):
        print("""
        Список комманд:
        help - вывести список комманд
        1 - показать заметки
        2 - добавить заметку
        3 - удалить заметку 
        4 - изменить заметку
        5 - сохранить заметки
        0 - выход
        """)

    def show(self):
        if self.notebook.len() == 0:
            print("Заметки отсутсвуют")
        else:
            mode = input("Введите 1, чтобы увидеть все заметки, или 2, чтобы выбрать временной промежуток: ")
            if mode is '1':
                self.notebook.show()
            if mode is '2':
                start_date = input("Введите дату начала в формате ГГГГ-ММ-ДД: ")
                try:
                    start_date = dt.strptime(start_date, '%Y-%m-%d')
                except:
                    print("Ошибка")
                end_date = input("Введите дату конца в формате ГГГГ-ММ-ДД: ")
                try:
                    end_date = dt.strptime(end_date, '%Y-%m-%d')
                except:
                    print("Ошибка")
                self.notebook.show(start_date, end_date)

    def add(self):
        title = input("Введите заголовок: ")
        body = input("Введите тело заметки: ")
        self.notebook.create_note(title, body)

    def edit(self):
        num = int(input("Введите номер заметки, которую хотите отредактировать: ")) - 1
        self.notebook.get_list()[num].set_title(input("Введите новый заголовок: "))
        self.notebook.get_list()[num].set_body(input("Введите новое тело заметки: "))

    def delete(self):
        num = int(input("Введите номер заметки, которую хотите удалить: ")) - 1
        self.notebook.delete_note(self.notebook.get_list()[num])

    def save(self):
        FileManager.save("notes.json", self.notebook.get_list())

    def exit(self):
        self.save()
        self.flag = False


