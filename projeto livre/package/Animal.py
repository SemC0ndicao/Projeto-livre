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
    def new_animal(cls):
        especie = input("what's the animal?\n")
        age = int(input("Type the age\n"))
        gender = input("Type the gender\n")
        breed = input("Type the breed\n")
        admission_date = datetime.datetime.now()
        admission_date = admission_date.strftime("%Y-%m-%d")
        tag = datetime.datetime.now()
        tag = (int(tag.strftime("%Y%m%d%H%M%S"))%99999)
        
        

        # Cria o dicionário com os dados
        data = {
            "tag": tag,
            "especie": especie,
            "age": age,
            "gender": gender,
            "breed": breed,
            "admission_date": admission_date
        }

        # Caminho do arquivo JSON
        base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"
        file_path = os.path.join(base_dir, "files", "animals.json")

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
    def list_animals(cls):
        Dog.list_dogs(cls)
        Cat.list_cats(cls)

        base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"

        try:
            
            
            file_path = os.path.join(base_dir, "files", "animals.json")

            with open(file_path, "r") as file:
                content = json.load(file)
                print("\n\n---------------------OTHERS---------------------\n\n")
                print(json.dumps(content, indent=4, ensure_ascii=False))

                
        except FileNotFoundError:
            pass
        except PermissionError:
            print("You do not have permission")

    
    @classmethod
    def edit_animal(cls):
        tag_input = input("Digite a TAG do animal que deseja editar:\n").strip()

        # Caminho do arquivo JSON
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "files", "animals.json")

        # Carrega os dados existentes
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    animals_data = json.load(f)
                except json.JSONDecodeError:
                    print("Erro ao carregar os dados existentes.")
                    return
        else:
            print("Arquivo de dados não encontrado.")
            return

        # Busca e edita o animal
        for idx, animal in enumerate(animals_data):
            if str(animal.get("tag")) == tag_input:
                print(f"\nAnimal encontrado (TAG: {animal['tag']}):")
                print(json.dumps(animal, indent=4))

                print("\nDigite os novos dados ou pressione Enter para manter os atuais.")

                especie = input(f"Espécie [{animal['especie']}]: ").strip() or animal['especie']
                age_input = input(f"Idade [{animal['age']}]: ").strip()
                age = int(age_input) if age_input else animal['age']
                gender = input(f"Gênero [{animal['gender']}]: ").strip() or animal['gender']
                breed = input(f"Raça [{animal['breed']}]: ").strip() or animal['breed']
                admission_date = animal['admission_date']  # não muda

                updated_data = {
                    "tag": animal["tag"],
                    "especie": especie,
                    "age": age,
                    "gender": gender,
                    "breed": breed,
                    "admission_date": admission_date
                }

                animals_data[idx] = updated_data

                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(animals_data, f, indent=4)

                print("\nAnimal atualizado com sucesso.")
                return cls(**updated_data)

        print("TAG não encontrada.")
        return None
    
    @classmethod
    def delete_animal(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        animals_path = os.path.join(base_dir, "files", "animals.json")

        if not os.path.exists(animals_path):
            print("No animals file found.")
            return

        with open(animals_path, "r", encoding="utf-8") as f:
            try:
                animals = json.load(f)
            except json.JSONDecodeError:
                print("Error reading animal data.")
                return

        tag = input("Animal tag to delete: ").strip()
        updated = [a for a in animals if str(a.get("tag")) != tag]

        if len(updated) == len(animals):
            print("Animal not found.")
            return

        with open(animals_path, "w", encoding="utf-8") as f:
            json.dump(updated, f, indent=4)

        print("Animal deleted.")       


#inherited
class Dog(Animal):

    def __init__(self, tag, especie, gender, breed, age, admission_date):
        super().__init__(tag, especie, gender, breed, age, admission_date)
    def bark():
         print("AUAU!")
    
    @classmethod
    def new_dog(cls):
        especie = "Dog"
        age = int(input("Type the age\n"))
        gender = input("Type the gender\n")
        breed = input("Type the breed\n")
        admission_date = datetime.datetime.now()
        admission_date = admission_date.strftime("%Y-%m-%d")
        tag = datetime.datetime.now()
        tag = (int(tag.strftime("%Y%m%d%H%M%S"))%99999)
        
        
        # Cria o dicionário com os dados
        data = {
            "tag": tag,
            "especie": especie,
            "age": age,
            "gender": gender,
            "breed": breed,
            "admission_date": admission_date
        }

        # Caminho do arquivo JSON
        base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"
        file_path = os.path.join(base_dir, "files", "dogs.json")

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
    
    
    
    def list_dogs(cls):

        base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"

        try:
            
            file_path = os.path.join(base_dir, "files", "dogs.json")

            with open(file_path, "r") as file:
                content = json.load(file)
                print("\n\n----------------------DOGS---------------------\n\n")
                print(json.dumps(content, indent=4, ensure_ascii=False))

                
        except FileNotFoundError:
            pass
        except PermissionError:
            print("You do not have permission")



    @classmethod
    def edit_dog(cls):
            tag_input = input("Digite a TAG do animal que deseja editar:\n").strip()

            # Caminho do arquivo JSON
            base_dir = os.path.dirname(os.path.dirname(__file__))
            file_path = os.path.join(base_dir, "files", "dogs.json")

            # Carrega os dados existentes
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        dogs_data = json.load(f)
                    except json.JSONDecodeError:
                        print("Erro ao carregar os dados existentes.")
                        return
            else:
                print("Arquivo de dados não encontrado.")
                return

            # Busca e edita o animal
            for idx, dog in enumerate(dogs_data):
                if str(dog.get("tag")) == tag_input:
                    print(f"\nAnimal encontrado (TAG: {dog['tag']}):")
                    print(json.dumps(dog, indent=4))

                    print("\nDigite os novos dados ou pressione Enter para manter os atuais.")

                    especie = input(f"Espécie [{dog['especie']}]: ").strip() or dog['especie']
                    age_input = input(f"Idade [{dog['age']}]: ").strip()
                    age = int(age_input) if age_input else dog['age']
                    gender = input(f"Gênero [{dog['gender']}]: ").strip() or dog['gender']
                    breed = input(f"Raça [{dog['breed']}]: ").strip() or dog['breed']
                    admission_date = dog['admission_date']  # não muda

                    updated_data = {
                        "tag": dog["tag"],
                        "especie": especie,
                        "age": age,
                        "gender": gender,
                        "breed": breed,
                        "admission_date": admission_date
                    }

                    dogs_data[idx] = updated_data

                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(dogs_data, f, indent=4)

                    print("\nDog updated succesfully.\n")
                    return cls(**updated_data)

            print("TAG não encontrada.")
            return None

    @classmethod
    def delete_dog(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        dogs_path = os.path.join(base_dir, "files", "dogs.json")

        if not os.path.exists(dogs_path):
            print("No dogs file found.")
            return

        with open(dogs_path, "r", encoding="utf-8") as f:
            try:
                dogs = json.load(f)
            except json.JSONDecodeError:
                print("Error reading dogs data.")
                return

        tag = input("dog tag to delete: ").strip()
        updated = [a for a in dogs if str(a.get("tag")) != tag]

        if len(updated) == len(dogs):
            print("Dog not found.")
            return

        with open(dogs_path, "w", encoding="utf-8") as f:
            json.dump(updated, f, indent=4)

        print("Dog deleted.")   


#inherited
class Cat(Animal):

    def __init__(self, tag, especie, gender, breed, age, admission_date):
        super().__init__(tag, especie, gender, breed, age, admission_date)
    def meow():
         print("Meow!")
    
    @classmethod
    def new_cat(cls):
        especie = "Cat"
        age = int(input("Type the age\n"))
        gender = input("Type the gender\n")
        breed = input("Type the breed\n")
        admission_date = datetime.datetime.now()
        admission_date = admission_date.strftime("%Y-%m-%d")
        tag = datetime.datetime.now()
        tag = (int(tag.strftime("%Y%m%d%H%M%S"))%99999)
        
        # Cria o dicionário com os dados
        data = {
            "tag": tag,
            "especie": especie,
            "age": age,
            "gender": gender,
            "breed": breed,
            "admission_date": admission_date
        }

        # Caminho do arquivo JSON
        base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"
        file_path = os.path.join(base_dir, "files", "cats.json")

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


    def list_cats(cls):

        base_dir = os.path.dirname(os.path.dirname(__file__))  # volta para "projeto livre"

        try:
                      
            file_path = os.path.join(base_dir, "files", "cats.json")

            with open(file_path, "r") as file:
                content = json.load(file)
                print("\n\n----------------------CATS---------------------\n\n")
                print(json.dumps(content, indent=4, ensure_ascii=False))     

                
        except FileNotFoundError:
            pass
        except PermissionError:
            print("You do not have permission")
    
    @classmethod
    def edit_cat(cls):
            tag_input = input("Digite a TAG do animal que deseja editar:\n").strip()

            # Caminho do arquivo JSON
            base_dir = os.path.dirname(os.path.dirname(__file__))
            file_path = os.path.join(base_dir, "files", "cats.json")

            # Carrega os dados existentes
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        cats_data = json.load(f)
                    except json.JSONDecodeError:
                        print("Erro ao carregar os dados existentes.")
                        return
            else:
                print("Arquivo de dados não encontrado.")
                return

            # Busca e edita o animal
            for idx, cat in enumerate(cats_data):
                if str(cat.get("tag")) == tag_input:
                    print(f"\nAnimal encontrado (TAG: {cat['tag']}):")
                    print(json.dumps(cat, indent=4))

                    print("\nDigite os novos dados ou pressione Enter para manter os atuais.")

                    especie = input(f"Espécie [{cat['especie']}]: ").strip() or cat['especie']
                    age_input = input(f"Idade [{cat['age']}]: ").strip()
                    age = int(age_input) if age_input else cat['age']
                    gender = input(f"Gênero [{cat['gender']}]: ").strip() or cat['gender']
                    breed = input(f"Raça [{cat['breed']}]: ").strip() or cat['breed']
                    admission_date = cat['admission_date']  # não muda

                    updated_data = {
                        "tag": cat["tag"],
                        "especie": especie,
                        "age": age,
                        "gender": gender,
                        "breed": breed,
                        "admission_date": admission_date
                    }

                    cats_data[idx] = updated_data

                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(cats_data, f, indent=4)

                    print("\nAnimal atualizado com sucesso.")
                    return cls(**updated_data)

            print("TAG não encontrada.")
            return None

    @classmethod
    def delete_cat(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        cats_path = os.path.join(base_dir, "files", "cats.json")

        if not os.path.exists(cats_path):
            print("No cats file found.")
            return

        with open(cats_path, "r", encoding="utf-8") as f:
            try:
                cats = json.load(f)
            except json.JSONDecodeError:
                print("Error reading cats data.")
                return

        tag = input("cat tag to delete: ").strip()
        updated = [a for a in cats if str(a.get("tag")) != tag]

        if len(updated) == len(cats):
            print("Cat not found.")
            return

        with open(cats_path, "w", encoding="utf-8") as f:
            json.dump(updated, f, indent=4)

        print("Cat deleted.") 