class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, postal_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._address = address
        self._city = city
        self._state = state
        self._postal_code = postal_code
        self._phone_number = phone_number
        self._emergency_contact_name = emergency_contact_name
        self._emergency_contact_phone = emergency_contact_phone

    def get_first_name(self):
        return self._first_name

    def get_middle_name(self):
        return self._middle_name

    def get_last_name(self):
        return self._last_name

    def get_address(self):
        return self._address

    def get_city(self):
        return self._city

    def get_state(self):
        return self._state

    def get_postal_code(self):
        return self._postal_code

    def get_phone_number(self):
        return self._phone_number

    def get_emergency_contact_name(self):
        return self._emergency_contact_name

    def get_emergency_contact_phone(self):
        return self._emergency_contact_phone

class Procedure:
    def __init__(self, name, date, doctor_name, cost):
        self._name = name
        self._date = date
        self._doctor_name = doctor_name
        self._cost = cost

    def get_name(self):
        return self._name

    def get_date(self):
        return self._date

    def get_doctor_name(self):
        return self._doctor_name

    def get_cost(self):
        return self._cost

    def set_name(self, name):
        self._name = name

    def set_date(self, date):
        self._date = date

    def set_doctor_name(self, doctor_name):
        self._doctor_name = doctor_name

    def set_cost(self, cost):
        self._cost = cost


if __name__ == "__main__":
    patient = Patient(
        first_name="Иван",
        middle_name="Иванович",
        last_name="Иванов",
        address="ул. Первая, д. 1",
        city="Город",
        state="Область",
        postal_code="12345",
        phone_number="123-456-7890",
        emergency_contact_name="Мария Ивановна",
        emergency_contact_phone="987-654-3210"
    )

    procedure1 = Procedure(name="Врачебный осмотр", date="Сегодняшняя", doctor_name="Ирвин", cost=250.00)
    procedure2 = Procedure(name="Рентгеноскопия", date="Сегодняшняя", doctor_name="Джемисон", cost=500.00)
    procedure3 = Procedure(name="Анализ крови", date="Сегодняшняя", doctor_name="Смит", cost=200.00)

    print("Информация о пациенте:")
    print("Имя:", patient.get_first_name())
    print("Отчество:", patient.get_middle_name())
    print("Фамилия:", patient.get_last_name())
    print("Адрес:", patient.get_address())
    print("Город:", patient.get_city())
    print("Область:", patient.get_state())
    print("Почтовый индекс:", patient.get_postal_code())
    print("Телефонный номер:", patient.get_phone_number())
    print("Контактное лицо:", patient.get_emergency_contact_name())
    print("Телефон контактного лица:", patient.get_emergency_contact_phone())

    print("\nИнформация о процедуре 1:")
    print("Название процедуры:", procedure1.get_name())
    print("Дата:", procedure1.get_date())
    print("Врач:", procedure1.get_doctor_name())
    print("Стоимость:", procedure1.get_cost())

    print("\nИнформация о процедуре 2:")
    print("Название процедуры:", procedure2.get_name())
    print("Дата:", procedure2.get_date())
    print("Врач:", procedure2.get_doctor_name())
    print("Стоимость:", procedure2.get_cost())

    print("\nИнформация о процедуре 3:")
    print("Название процедуры:", procedure3.get_name())
    print("Дата:", procedure3.get_date())
    print("Врач:", procedure3.get_doctor_name())
    print("Стоимость:", procedure3.get_cost())

    total_cost = procedure1.get_cost() + procedure2.get_cost() + procedure3.get_cost()
    print("\nОбщая стоимость всех процедур:", total_cost)
