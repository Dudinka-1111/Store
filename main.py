class Store():

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")

# Создание объектов класса Store
store1 = Store("Магнит", "Улица Пушикна, 76")
store2 = Store("Пятерочка", "Комсомольский проспект, 45")
store3 = Store("ЛЕНТА", "Улица Пушкина, 80")

# Добавление товаров в магазины
store1.add_item("яблоки", 123)
store1.add_item("бананы", 150)

store2.add_item("апельсины", 202)
store2.add_item("груши", 237)

store3.add_item("виноград", 198)
store3.add_item("персики", 256)

# Тестирование методов на одном из магазинов
print("\nТестирование методов в 'Магнит на Улице Пушкина,76':")

# Добавление товара
store1.add_item("груши", 230)

# Обновление цены товара
store1.update_price("бананы", 133)

# Удаление товара
store1.remove_item("яблоки")

# Запрос цены товара
price = store1.get_price("бананы")
if price is not None:
    print(f"Цена бананов: {price}")
else:
    print("Бананы отсутствуют в ассортименте.")
