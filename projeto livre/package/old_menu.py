import Animal, Dog, Cat
from Adopter import Adopter
from Contract import Contract


#1 animal
#2 adopter
#3 contracts

#new animal
#edit animal
#delete animal
#list animals
class Menu():

    def __init__(self):
        self.option = None
        while self.option != "0" :
            self.menu = {
                    "1": self.animal_menu,
                    "2": self.adopter_menu,
                    "3": self.contract_menu,    
                    "0": self.out       
                }
            self.option = input("\n1 - Animais\n2 - Adopters\n3 - Contracts\n0 - Exit\n")
            self.menu.get(self.option, self.warning)()
            





    def animal_menu(self):
        self.menu = {
            "1": self.new_animal,
            "2": self.list_animals,
            "3": self.edit_animal,
            "4": self.delete_animal

        }

        option = input("\n 1 - new animal\n 2 - list animal\n 3 - edit animal\n 4 - delete animal\n")
        self.menu.get(option, self.warning)()
        if option == "0" :
            return
        
    def new_animal(self):
        opcao = input("\nQual a espécie?\n 1 - Cachorro\n 2 - Gato\n 3 - Outro\n")

        if opcao == "1":
            Dog.new_dog()
        elif opcao == "2":
            Cat.new_cat()
        elif opcao == "3":
            Animal.new_animal()
        else:
            print("\nSelecione uma opção válida!\n")
    
    def list_animals(self):

        Animal.list_animals()

    def edit_animal(self):
    
        opcao = input("\nQual a espécie?\n 1 - Cachorro\n 2 - Gato\n 3 - Outro\n")

        if opcao == "1":
            Dog.edit_dog()
        elif opcao == "2":
            Cat.edit_cat()
        elif opcao == "3":
            Animal.edit_animal()
        else:
            print("\nSelecione uma opção válida!\n")  
        

    def delete_animal(self):

        opcao = input("\nQual a espécie?\n 1 - Cachorro\n 2 - Gato\n 3 - Outro\n")

        if opcao == "1":
            Dog.Dog.delete_dog()
        elif opcao == "2":
            Cat.delete_cat()
        elif opcao == "3":
            Animal.delete_animal()
        else:
            print("\nSelecione uma opção válida!\n") 







    def adopter_menu(self):
        self.menu = {
            "1": self.new_adopter,
            "2": self.list_adopters,
            "3": self.edit_adopter,
            "4": self.delete_adopter

        }

        option = input("\n 1 - new adopter\n 2 - list adopter\n 3 - edit adopter\n 4 - delete adopter\n")
        self.menu.get(option, self.warning)()
        if option == "0" :
            return

    def new_adopter(self):
        Adopter.new_adopter()
    
    def list_adopters(self):
        Adopter.list_adopters()

    def edit_adopter(self):
        Adopter.edit_adopter()

    def delete_adopter(self):
        Adopter.delete_adopter()





    def contract_menu(self):
        
        self.menu = {
            "1": self.new_contract,
            "2": self.list_contracts,
            "3": self.edit_contract,
            "4": self.delete_contract

        }

        option = input("\n 1 - new contract\n 2 - list contracts\n 3 - edit contracts\n 4 - delete contract\n")
        self.menu.get(option, self.warning)()
        if option == "0" :
            return

    def new_contract(self):
        Contract.new_contract()

    def list_contracts(self):
        Contract.list_contracts()

    def edit_contract(self):
        Contract.edit_contract()

    def delete_contract(self):
        Contract.delete_contract()





    def warning(self):
        print("\nEscolha uma opção válida!\n")
    
    def out(self):
        self.option = "0"
