from Product import Product
from magazin import Magizin

def vvod_number(str, b):
    while True:
        try:
            a = int(input(str))
            if b == 1:
                if 1 <= a <= 2:
                    return a
            else:
                return a
        except:
            print("Это не число")

magazin = Magizin(input("Введите название магазина: "))

while True:
    print("1. Добавить продукт\n2. Удалить продукт\n3. Выгруить все продукты")
    vibor = vvod_number("Выбор: ", 0)
    if vibor == 1:
        name = input("Введите название продукта: ")
        price = vvod_number("Введите цену продукта", 0)
        print("1. Фрукты\n2. Овощи")
        type_num = vvod_number("Выберите номер продукта: ", 1)
        if type_num == 1:
            type = 'Фрукты'
        elif type_num == 2:
            type = 'Овощи'
        product = Product(name, price, type)
        magazin.add_product(product)
    elif vibor == 2:
        magazin.show_all()
        vib = vvod_number("Введите номер продукта:", 0)
        magazin.delete_product(vib)
    elif vibor == 3:
        magazin.show_all()
    else:
        print("Такого выбора нет")
