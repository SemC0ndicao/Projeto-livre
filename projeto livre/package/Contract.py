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
        contracts_path = os.path.join(base_dir, "files", "contracts.json")

        # Load adopters
        if os.path.exists(adopters_path):
            with open(adopters_path, "r", encoding="utf-8") as f:
                adopters = json.load(f)
        else:
            adopters = []

        # Load animals
        if os.path.exists(animals_path):
            with open(animals_path, "r", encoding="utf-8") as f:
                animals = json.load(f)
        else:
            animals = []

        cpf = input("\nWhat's the cpf of the adopter? \n")

        found_adopter = next((a for a in adopters if a.get("cpf") == cpf), None)
        if not found_adopter:
            print("Adopter not found.")
            return

        print("\nAvailable animals:")
        for animal in animals:
            print(f"\nTag: {animal['tag']} |\n Species: {animal['especie']} |\n Breed: {animal['breed']}\n")

        animal_tag = input("\nEnter the tag of the animal: ").strip()

        found_animal = next((a for a in animals if str(a.get("tag")) == animal_tag), None)
        if not found_animal:
            print("\nAnimal not found.\n")
            return

        contract_date = datetime.datetime.now().strftime("%Y-%m-%d")

        contract = {
            "cpf": cpf,
            "animal_tag": animal_tag,
            "date": contract_date
        }

        if os.path.exists(contracts_path):
            with open(contracts_path, "r", encoding="utf-8") as f:
                try:
                    existing_contracts = json.load(f)
                except json.JSONDecodeError:
                    existing_contracts = []
        else:
            existing_contracts = []

        existing_contracts.append(contract)

        with open(contracts_path, "w", encoding="utf-8") as f:
            json.dump(existing_contracts, f, indent=4)

        print("\nContract created successfully.\n")
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
                        print(f"Adopter: {c['cpf']} |\n Animal Tag: {c['animal_tag']} |\n Date: {c['date']}\n")
                except json.JSONDecodeError:
                    print("Contracts file is empty or corrupted.")
        else:
            print("\nNo contracts found.\n")

    @classmethod
    def edit_contract(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        contracts_path = os.path.join(base_dir, "files", "contracts.json")

        if not os.path.exists(contracts_path):
            print("\nNo contracts found.\n")
            return

        with open(contracts_path, "r", encoding="utf-8") as f:
            try:
                contracts = json.load(f)
            except json.JSONDecodeError:
                print("\nError reading contracts.\n")
                return

        cpf = input("\nEnter adopter's cpf: ").strip()
        tag = input("\nEnter animal tag: ").strip()

        for i, c in enumerate(contracts):
            if c["cpf"] == cpf and str(c["animal_tag"]) == tag:
                print(f"Contract found:\nAdopter: {c['cpf']}\nTag: {c['animal_tag']}\nDate: {c['date']}")
                print("\nLeave empty to keep current value.")

                new_cpf = input(f"New adopter cpf [{c['cpf']}]: ").strip() or c['cpf']
                new_tag = input(f"New animal tag [{c['animal_tag']}]: ").strip() or c['animal_tag']
                new_date = input(f"New date [{c['date']}]: ").strip() or c['date']

                updated_contract = {
                    "cpf": new_cpf,
                    "animal_tag": new_tag,
                    "date": new_date
                }

                contracts[i] = updated_contract

                with open(contracts_path, "w", encoding="utf-8") as f:
                    json.dump(contracts, f, indent=4)

                print("\nContract updated successfully.\n")
                return cls(**updated_contract)

        print("\nContract not found.\n")
        return None
    

    @classmethod
    def delete_contract(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        contracts_path = os.path.join(base_dir, "files", "contracts.json")

        if not os.path.exists(contracts_path):
            print("\nNo contracts to delete.\n")
            return

        with open(contracts_path, "r", encoding="utf-8") as f:
            try:
                contracts = json.load(f)
            except json.JSONDecodeError:
                print("Error loading contracts.")
                return

        cpf = input("\nEnter adopter's cpf: ").strip()
        tag = input("\nEnter animal tag: ").strip()

        new_contracts = [c for c in contracts if not (c["cpf"] == cpf and str(c["animal_tag"]) == tag)]

        if len(new_contracts) == len(contracts):
            print("\nContract not found.\n")
            return

        with open(contracts_path, "w", encoding="utf-8") as f:
            json.dump(new_contracts, f, indent=4)

        print("\nContract deleted successfully.\n")