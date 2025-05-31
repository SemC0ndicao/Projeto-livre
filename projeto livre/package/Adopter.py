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


    @classmethod
    def edit_adopter(cls):
            cpf_input = input("Type the CPF of the adopter you want to edit:\n").strip()

            # Caminho do arquivo JSON
            base_dir = os.path.dirname(os.path.dirname(__file__))
            file_path = os.path.join(base_dir, "files", "adopters.json")

            # Carrega os dados existentes
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        adopters_data = json.load(f)
                    except json.JSONDecodeError:
                        print("Erro ao carregar os dados existentes.")
                        return
            else:
                print("Arquivo de dados não encontrado.")
                return

            # Busca e edita o animal
            for idx, adopter in enumerate(adopters_data):
                if str(adopter.get("cpf")) == cpf_input:
                    print(f"\nAnimal encontrado (CPF: {adopter['cpf']}):")
                    print(json.dumps(adopter, indent=4))

                    print("\nDigite os novos dados ou pressione Enter para manter os atuais.")

                    name = input(f"Name [{adopter['name']}]: ").strip() or adopter['name']
                    birth_date = input(f"Birth date [{adopter['birth_date']}]: ").strip() or adopter['birth_date']
                    cpf = input(f"CPF [{adopter['cpf']}]: ").strip() or adopter['cpf']
                    

                    updated_data = {
                        "name": name,
                        "birth_date": birth_date,
                        "cpf": cpf
                    }

                    adopters_data[idx] = updated_data

                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(adopters_data, f, indent=4)

                    print("\nAnimal atualizado com sucesso.")
                    return cls(**updated_data)

            print("CPF não encontrado.")
            return None

   