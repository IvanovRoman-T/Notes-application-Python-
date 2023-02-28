import json
import datetime
from Note import Note


class Notebook:
    __notebook = None

    def __init__(self):
        self.__notebook = []

    def get_list(self):
        return self.__notebook

    def create_note(self, title, body):
        self.__notebook.append(Note(title, body))

    def create_note_from_json(self, new_note):
        new_note: str = json.loads(new_note)
        list_ = new_note.split(';')
        self.__notebook.append(Note(list_[1],
                                    list_[2],
                                    datetime.datetime.strptime(list_[3], '%Y-%m-%d %H:%M:%S.%f'),
                                    int(list_[0])))

    def delete_note(self, id):
        for note in self.__notebook:
            if note.get_id() == id:
                self.__notebook.remove(note)

    def edit_title(self, id, new_title):
        for note in self.__notebook:
            if note.get_id() == id:
                note.set_title(new_title)

    def edit_body(self, id, new_body):
        for note in self.__notebook:
            if note.get_id() == id:
                note.set_body(new_body)

    def len(self):
        return len(self.__notebook)

    def show(self, start_date=None, end_date=None):
        self.__notebook = sorted(self.__notebook)
        for note in self.__notebook:
            if start_date <= note.get_date() <= end_date:
                print(note, end='\n\n')
