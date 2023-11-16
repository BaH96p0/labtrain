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

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_middle_name(self, middle_name):
        self._middle_name = middle_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_address(self, address):
        self._address = address

    def set_city(self, city):
        self._city = city

    def set_state(self, state):
        self._state = state

    def set_postal_code(self, postal_code):
        self._postal_code = postal_code

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_emergency_contact_name(self, emergency_contact_name):
        self._emergency_contact_name = emergency_contact_name

    def set_emergency_contact_phone(self, emergency_contact_phone):
        self._emergency_contact_phone = emergency_contact_phone


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
