from .Animal import Animal
from .mixins import JsonStorableMixin
import datetime

class Cat(Animal, JsonStorableMixin):
    def __init__(self, tag, especie, gender, breed, age, admission_date):
        super().__init__(tag, especie, gender, breed, age, admission_date)

    @classmethod
    def new_cat(cls, breed, gender, age):
        especie = "Cat"
        now = datetime.datetime.now()
        tag = int(now.strftime("%Y%m%d%H%M%S")) % 99999
        admission_date = now.strftime("%Y-%m-%d")
        cat = {
            "tag": str(tag),
            "especie": especie,
            "gender": gender,
            "breed": breed,
            "age": age,
            "admission_date": admission_date
        }
        data = cls.load_all("cats.json")
        data.append(cat)
        cls.save_all("cats.json", data)
        return cls(**cat)