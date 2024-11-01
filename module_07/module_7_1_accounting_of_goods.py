class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
        """Метод get_products(self), который считывает всю информацию из файла __file_name,
        закрывает его и возвращает единую строку со всеми товарами из файла __file_name."""
        file = open(self.__file_name, 'r')
        info = file.read()
        file.close()
        return info

    def add(self, *products):
        """принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' ."""

        existing_products = self.get_products().splitlines()
        existing_product_names = []
        for product in existing_products:
            existing_product_names.append(product.split(', ')[0])

        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in existing_product_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(f'{product}\n')

        file.close()


# test
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

