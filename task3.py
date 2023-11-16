class Pet:
    def __init__(self, name, animal_type, age):
        self._name = name
        self._animal_type = animal_type
        self._age = age

    def set_name(self, name):
        self._name = name

    def set_animal_type(self, animal_type):
        self._animal_type = animal_type

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_animal_type(self):
        return self._animal_type

    def get_age(self):
        return self._age


if __name__ == "__main__":
    pet_name = input("Введите имя вашего домашнего животного: ")
    pet_type = input("Введите тип домашнего животного (например, 'собака', 'кот', 'птица'): ")
    pet_age = input("Введите возраст домашнего животного: ")

    # Создаем объект класса Pet
    my_pet = Pet(name=pet_name, animal_type=pet_type, age=pet_age)

    print("\nИнформация о вашем домашнем животном:")
    print("Имя:", my_pet.get_name())
    print("Тип:", my_pet.get_animal_type())
    print("Возраст:", my_pet.get_age())
