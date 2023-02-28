import json
import os.path


class FileManager:
    @staticmethod
    def read(file_name, notebook):
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                a = json.load(f)
                for e in a:
                    notebook.create_note_from_json(e)

    @staticmethod
    def save(file_name, list_):
        for i in range(len(list_)):
            list_[i] = list_[i].to_json()
        f = open(file_name, 'w')
        json.dump(list_, f)
        f.close()

