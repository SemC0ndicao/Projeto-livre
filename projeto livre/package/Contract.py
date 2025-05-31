import json
import os
import datetime

class Contract:
    def __init__(self, cpf, animal_tag, date):
        self.cpf = cpf
        self.animal_tag = animal_tag
        self.date = date

    @classmethod
    def new_contract(cls, cpf, animal_tag):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        contracts_path = os.path.join(base_dir, "files", "contracts.json")

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

        return cls(**contract)

    @classmethod
    def delete_contract(cls, cpf, animal_tag):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        contracts_path = os.path.join(base_dir, "files", "contracts.json")

        if not os.path.exists(contracts_path):
            return False

        with open(contracts_path, "r", encoding="utf-8") as f:
            try:
                contracts = json.load(f)
            except json.JSONDecodeError:
                return False

        updated = [c for c in contracts if not (c.get("cpf") == cpf and str(c.get("animal_tag")) == str(animal_tag))]

        if len(updated) == len(contracts):
            return False

        with open(contracts_path, "w", encoding="utf-8") as f:
            json.dump(updated, f, indent=4)

        return True