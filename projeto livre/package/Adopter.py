import json
import os

class Adopter():
    def __init__(self, name, birth_date, cpf):
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
    
    @classmethod
    def new_adopter(cls):
        name = input("Type the full name\n") 
        birth_date = input("type the birth date\n")
        cpf = input("Type the cpf\n")

    # Cria o dicionário com os dados
        data = {
            "name": name,
            "birth_date": birth_date,
            "cpf": cpf
        }

        # Caminho do arquivo JSON
        base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"
        file_path = os.path.join(base_dir, "files", "adopters.json")

        # Verifica se já existe conteúdo no arquivo
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        # Adiciona o novo animal
        existing_data.append(data)

        # Grava no arquivo
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4)

        return cls(**data)  
    
    @classmethod
    def list_adopters(cls):

        base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"

        try:
            
            file_path = os.path.join(base_dir, "files", "adopters.json")

            with open(file_path, "r") as file:
                content = json.load(file)
                print("\n\n----------------------ADOPTERS---------------------\n\n")
                print(json.dumps(content, indent=4, ensure_ascii=False))
                print("\n\n")
            
        except FileNotFoundError:
            print("That file was not found\n")
        except PermissionError:
            print("You do not have permission\n")

   