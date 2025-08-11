class Product:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def get_info(self):
        print(f"Название: {self.name}")
        print(f"Цена: {self.price}")
        print(f"Тип: {self.type}")