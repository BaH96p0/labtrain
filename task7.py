class RetailItem:
    def __init__(self, description, quantity_on_hand, price):
        self._description = description
        self._quantity_on_hand = quantity_on_hand
        self._price = price

    def get_description(self):
        return self._description

    def get_quantity_on_hand(self):
        return self._quantity_on_hand

    def get_price(self):
        return self._price


if __name__ == "__main__":
    item1 = RetailItem(description="Пиджак", quantity_on_hand=12, price=59.95)
    item2 = RetailItem(description="Дизайнерские джинсы", quantity_on_hand=40, price=34.95)
    item3 = RetailItem(description="Рубашка", quantity_on_hand=20, price=24.95)

    print("Информация о товаре 1:")
    print("Описание:", item1.get_description())
    print("Количество на складе:", item1.get_quantity_on_hand())
    print("Цена:", item1.get_price())

    print("\nИнформация о товаре 2:")
    print("Описание:", item2.get_description())
    print("Количество на складе:", item2.get_quantity_on_hand())
    print("Цена:", item2.get_price())

    print("\nИнформация о товаре 3:")
    print("Описание:", item3.get_description())
    print("Количество на складе:", item3.get_quantity_on_hand())
    print("Цена:", item3.get_price())
