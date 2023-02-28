from Note import Note
import json


class FileManager:
    @staticmethod
    def read(file_name):
        with open(file_name, 'r') as f:
            a = json.load(f)
            for e in a:
                Note.create_note(e)

    @staticmethod
    def