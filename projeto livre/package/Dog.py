from .Animal import Animal
from .mixins import JsonStorableMixin
import datetime

class Dog(Animal, JsonStorableMixin):
    def __init__(self, tag, especie, gender, breed, age, admission_date):
        super().__init__(tag, especie, gender, breed, age, admission_date)

    @classmethod
    def new_dog(cls, breed, gender, age):
        especie = "Dog"
        now = datetime.datetime.now()
        tag = int(now.strftime("%Y%m%d%H%M%S")) % 99999
        admission_date = now.strftime("%Y-%m-%d")
        dog = {
            "tag": str(tag),
            "especie": especie,
            "gender": gender,
            "breed": breed,
            "age": age,
            "admission_date": admission_date
        }
        data = cls.load_all("dogs.json")
        data.append(dog)
        cls.save_all("dogs.json", data)
        return cls(**dog)