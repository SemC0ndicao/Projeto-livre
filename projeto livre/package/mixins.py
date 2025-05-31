import os
import json

class JsonStorableMixin:
    @staticmethod
    def get_file_path(filename):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        return os.path.join(base_dir, "files", filename)

    @classmethod
    def load_all(cls, filename):
        path = cls.get_file_path(filename)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    @classmethod
    def save_all(cls, filename, data):
        path = cls.get_file_path(filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)