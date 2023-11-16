class Employee:
    def __init__(self, name, id_number, department, position):
        self._name = name
        self._id_number = id_number
        self._department = department
        self._position = position

    def get_name(self):
        return self._name

    def get_id_number(self):
        return self._id_number

    def get_department(self):
        return self._department

    def get_position(self):
        return self._position


if __name__ == "__main__":
    employee1 = Employee(name="Сьюзан Мейерс", id_number=47899, department="Бухгалтерия", position="Вице-президент")
    employee2 = Employee(name="Марк Джоунс", id_number=39119, department="ИТ", position="Программист")
    employee3 = Employee(name="Джой Роджерс", id_number=81774, department="Производственный", position="Инженер")

    print("Информация о сотруднике 1:")
    print("Имя:", employee1.get_name())
    print("Идентификационный номер:", employee1.get_id_number())
    print("Отдел:", employee1.get_department())
    print("Должность:", employee1.get_position())

    print("\nИнформация о сотруднике 2:")
    print("Имя:", employee2.get_name())
    print("Идентификационный номер:", employee2.get_id_number())
    print("Отдел:", employee2.get_department())
    print("Должность:", employee2.get_position())

    print("\nИнформация о сотруднике 3:")
    print("Имя:", employee3.get_name())
    print("Идентификационный номер:", employee3.get_id_number())
    print("Отдел:", employee3.get_department())
    print("Должность:", employee3.get_position())
