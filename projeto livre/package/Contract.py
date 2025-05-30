from .Animal import Animal
from .Adopter import Adopter
import datetime
import json
import os

class Adoption_contract():
      def __init__(self, animal, adopter, contract_date):
            self.animal = animal
            self.adopter = adopter
            self.contract_date = contract_date
      
      @classmethod
      def new_contract(cls):
            print("\n\n----------------------AVAIABLE ANIMALS---------------------\n\n")
            Animal.list_animals()
            animal = input("type the tag of the animal you want\n")

            print("\n\n----------------------REGISTERED ADOPTERS---------------------\n\n")
            Adopter.list_adopters() 
            adopter = input("type the cpf of the adopter")

            contract_date = datetime.datetime.now()
            contract_date = contract_date.strftime("%Y-%m-%d") 
            
            
            
            # Cria o dicionário com os dados
            data = {
                  "animal": animal,
                  "adopter": adopter,
                  "contract_date": contract_date
            }

            # Caminho do arquivo JSON
            base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"
            file_path = os.path.join(base_dir, "files", "contracts.json")

            # Verifica se já existe conteúdo no arquivo
            if os.path.exists(file_path):
                  with open(file_path, "r", encoding="utf-8") as f:
                        try:
                              
                              existing_data = json.load(f)
                        except json.JSONDecodeError:
                              existing_data = []
            else:
                  existing_data = []

            # Adiciona o novo contrato
            existing_data.append(data)

            # Grava no arquivo
            with open(file_path, "w", encoding="utf-8") as f:
                  json.dump(existing_data, f, indent=4)

            return cls(**data)
      
      @classmethod
      def list_contracts(cls):

            base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"

            try:
                  
                  file_path = os.path.join(base_dir, "files", "contracts.json")

                  with open(file_path, "r") as file:
                        content = json.load(file)
                        print("\n\n----------------------CONTRACTS---------------------\n\n")
                        print(json.dumps(content, indent=4, ensure_ascii=False))
                        print("\n\n")
                  
            except FileNotFoundError:
                  print("That file was not found\n")
            except PermissionError:
                  print("You do not have permission\n")


    

