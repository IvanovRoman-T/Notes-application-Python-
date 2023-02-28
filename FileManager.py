import json
import os.path


class FileManager:
    # чтение заметок из файла
    @staticmethod
    def read(file_name, notebook):
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                a = json.load(f)
                for e in a:
                    notebook.create_note_from_json(e)

    # сохранение заметок в файл
    @staticmethod
    def save(file_name, list_):
        list1 = []
        for i in range(len(list_)):
            list1.append(list_[i].to_json())
        f = open(file_name, 'w')
        json.dump(list1, f)
        f.close()

