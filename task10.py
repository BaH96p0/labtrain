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


class CashRegister:
    def __init__(self):
        self._items = []

    def purchase_item(self, item):
        self._items.append(item)

    def get_total(self):
        total = 0
        for item in self._items:
            total += item.get_price()
        return total

    def show_items(self):
        print("Товары в корзине:")
        for item in self._items:
            print(f"Описание: {item.get_description()}, Цена: {item.get_price()}")

    def clear(self):
        self._items = []


if __name__ == "__main__":
    item1 = RetailItem(description="Пиджак", quantity_on_hand=12, price=59.95)
    item2 = RetailItem(description="Дизайнерские джинсы", quantity_on_hand=40, price=34.95)
    item3 = RetailItem(description="Рубашка", quantity_on_hand=20, price=24.95)

    register = CashRegister()

    register.purchase_item(item1)
    register.purchase_item(item2)
    register.purchase_item(item3)

    register.show_items()
    print(f"\nОбщая стоимость покупки: {register.get_total():.2f}")
