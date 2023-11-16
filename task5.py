class Information:
    def __init__(self, name, address, age, phone_number):
        self._name = name
        self._address = address
        self._age = age
        self._phone_number = phone_number

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age

    def get_phone_number(self):
        return self._phone_number

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_age(self, age):
        self._age = age

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number


if __name__ == "__main__":
    my_info = Information(name="Ваше имя", address="Ваш адрес", age=25, phone_number="Ваш номер телефона")
    friend1_info = Information(name="Друг 1", address="Адрес друга 1", age=30, phone_number="Номер телефона друга 1")
    friend2_info = Information(name="Друг 2", address="Адрес друга 2", age=28, phone_number="Номер телефона друга 2")

    print("Ваша информация:")
    print("Имя:", my_info.get_name())
    print("Адрес:", my_info.get_address())
    print("Возраст:", my_info.get_age())
    print("Телефонный номер:", my_info.get_phone_number())

    print("\nИнформация о друге 1:")
    print("Имя:", friend1_info.get_name())
    print("Адрес:", friend1_info.get_address())
    print("Возраст:", friend1_info.get_age())
    print("Телефонный номер:", friend1_info.get_phone_number())

    print("\nИнформация о друге 2:")
    print("Имя:", friend2_info.get_name())
    print("Адрес:", friend2_info.get_address())
    print("Возраст:", friend2_info.get_age())
    print("Телефонный номер:", friend2_info.get_phone_number())
