class Car:
    def __init__(self, year_model, make):
        self._year_model = year_model
        self._make = make
        self._speed = 0

    def accelerate(self):
        self._speed += 5

    def brake(self):
        if self._speed >= 5:
            self._speed -= 5
        else:
            self._speed = 0

    def get_speed(self):
        return self._speed


if __name__ == "__main__":
    # Создаем объект класса Car
    my_car = Car(year_model=2022, make="Toyota")

    print("Ускоряемся:")
    for _ in range(5):
        my_car.accelerate()
        print("Текущая скорость:", my_car.get_speed())

    print("\nТормозим:")
    for _ in range(5):
        my_car.brake()
        print("Текущая скорость:", my_car.get_speed())
