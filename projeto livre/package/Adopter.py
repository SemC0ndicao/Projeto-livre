import json
import os

class Adopter:
    def __init__(self, cpf, name, phone):
        self.cpf = cpf
        self.name = name
        self.phone = phone

    @classmethod
    def new_adopter(cls, cpf, name, phone):
        data = {
            "cpf": cpf,
            "name": name,
            "phone": phone
        }

        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "files", "adopters.json")

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    existing = json.load(f)
                except json.JSONDecodeError:
                    existing = []
        else:
            existing = []

        existing.append(data)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=4)

        return cls(**data)

    @classmethod
    def delete_adopter(cls, cpf):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "files", "adopters.json")

        if not os.path.exists(file_path):
            return False

        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return False

        updated = [a for a in data if a.get("cpf") != cpf]

        if len(updated) == len(data):
            return False

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(updated, f, indent=4)

        return True