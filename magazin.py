class Magizin:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
        else:
            print("Такой продукт уже есть")

    def delete_product(self, id_produt):
        if 0 <= id_produt < len(self.products):
            self.products.pop(id_produt)
        else:
            print("Продукт нельзя удалить")

    def show_all(self):
        for number, i in enumerate(self.products):
            print(number, end=' ')
            i.get_info()
            print('-'*20)
