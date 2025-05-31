import json
import os
import datetime

class Contract:
      def __init__(self, cpf, animal_tag, date):
            self.cpf = cpf
            self.animal_tag = animal_tag
            self.date = date

      @classmethod
      def new_contract(cls):
            base_dir = os.path.dirname(os.path.dirname(__file__))
            adopters_path = os.path.join(base_dir, "files", "adopters.json")
            animals_path = os.path.join(base_dir, "files", "animals.json")
            dogs_path = os.path.join(base_dir, "files", "dogs.json")
            cats_path = os.path.join(base_dir, "files", "cats.json")
            contracts_path = os.path.join(base_dir, "files", "contracts.json")

            def load_json(path):
                  if os.path.exists(path):
                        with open(path, "r", encoding="utf-8") as f:
                              try:
                                    return json.load(f)
                              except json.JSONDecodeError:
                                    return []
                  return []

            adopters = load_json(adopters_path)
            animals = load_json(animals_path)
            dogs = load_json(dogs_path)
            cats = load_json(cats_path)

            all_animals = animals + dogs + cats

            cpf = input("Adopter CPF: ").strip()
            adopter = next((a for a in adopters if a.get("cpf") == cpf), None)
            if not adopter:
                  print("Adopter not found.")
                  return

            print("\nAvailable animals:")
            for animal in all_animals:
                  print(f"[{animal['tag']}] {animal['especie']} - {animal['breed']}")

            animal_tag = input("Animal tag: ").strip()
            animal = next((a for a in all_animals if str(a.get("tag")) == animal_tag), None)
            if not animal:
                  print("Animal not found.")
                  return

            contract_date = datetime.datetime.now().strftime("%Y-%m-%d")
            contract = {
                  "cpf": cpf,
                  "animal_tag": animal_tag,
                  "date": contract_date
            }

            existing_contracts = load_json(contracts_path)
            existing_contracts.append(contract)

            with open(contracts_path, "w", encoding="utf-8") as f:
                  json.dump(existing_contracts, f, indent=4)

            print("Contract successfully created.")
            return cls(**contract)


      @classmethod
      def list_contracts(cls):
            base_dir = os.path.dirname(os.path.dirname(__file__))
            contracts_path = os.path.join(base_dir, "files", "contracts.json")

            if os.path.exists(contracts_path):
                  with open(contracts_path, "r", encoding="utf-8") as f:
                        try:
                              contracts = json.load(f)
                              for c in contracts:
                                    print(f"Contract => Adopter: {c['cpf']} | Tag: {c['animal_tag']} | Date: {c['date']}")
                        except json.JSONDecodeError:
                              print("Contracts file is empty or corrupted.")
            else:
                  print("No contracts found.")

      @classmethod
      def edit_contract(cls):
            base_dir = os.path.dirname(os.path.dirname(__file__))
            contracts_path = os.path.join(base_dir, "files", "contracts.json")

            if not os.path.exists(contracts_path):
                  print("No contracts found.")
                  return

            with open(contracts_path, "r", encoding="utf-8") as f:
                  try:
                        contracts = json.load(f)
                  except json.JSONDecodeError:
                        print("Error reading contracts.")
                        return

            cpf = input("Adopter CPF: ").strip()
            tag = input("Animal tag: ").strip()

            for i, c in enumerate(contracts):
                  if c["cpf"] == cpf and str(c["animal_tag"]) == tag:
                        print(f"Contract found: Adopter: {c['cpf']} | Tag: {c['animal_tag']} | Date: {c['date']}")
                        print("Leave blank to keep current value.")

                        new_cpf = input("New CPF: ").strip()
                        new_tag = input("New animal tag: ").strip()

                        if new_cpf:
                              contracts[i]["cpf"] = new_cpf
                        if new_tag:
                              contracts[i]["animal_tag"] = new_tag

                        with open(contracts_path, "w", encoding="utf-8") as f:
                              json.dump(contracts, f, indent=4)

                              print("Contract updated.")
                              return  # <- ESSENCIAL!

            print("Contract not found.")
            return None

      @classmethod
      def delete_contract(cls):
            base_dir = os.path.dirname(os.path.dirname(__file__))
            contracts_path = os.path.join(base_dir, "files", "contracts.json")

            if not os.path.exists(contracts_path):
                  print("No contracts found.")
                  return

            with open(contracts_path, "r", encoding="utf-8") as f:
                  try:
                        contracts = json.load(f)
                  except json.JSONDecodeError:
                        print("Error reading contracts.")
                        return

            cpf = input("Adopter CPF: ").strip()
            tag = input("Animal tag: ").strip()

            filtered_contracts = [
                  c for c in contracts
            if not (c["cpf"] == cpf and str(c["animal_tag"]) == tag)
            ]

            if len(filtered_contracts) == len(contracts):
                  print("Contract not found.")
                  return

            with open(contracts_path, "w", encoding="utf-8") as f:
                  json.dump(filtered_contracts, f, indent=4)

            print("Contract deleted.")

