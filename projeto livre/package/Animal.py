import datetime
import json
import os


class Animal():
    def __init__(self, tag, especie, gender, breed, age, admission_date): 
        self.tag = tag
        self.especie = especie
        self.age = age
        self.gender = gender
        self.breed = breed
        self.admission_date = admission_date

    @classmethod
    def new_animal(cls, especie, age, gender, breed):
        now = datetime.datetime.now()
        admission_date = now.strftime("%Y-%m-%d")
        tag = int(now.strftime("%Y%m%d%H%M%S")) % 99999

        data = {
            "tag": str(tag),
            "especie": especie,
            "age": age,
            "gender": gender,
            "breed": breed,
            "admission_date": admission_date
        }

        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "files", "animals.json")

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        existing_data.append(data)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4)

        return cls(**data)

    @classmethod
    def delete_animal(cls, tag):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "files", "animals.json")

        if not os.path.exists(file_path):
            return False

        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return False

        updated = [a for a in data if str(a.get("tag")) != str(tag)]
        if len(updated) == len(data):
            return False

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(updated, f, indent=4)

        return True