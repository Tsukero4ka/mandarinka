class Product:
    __slots__ = ['name', 'price']

    def __init__(self, name, price):
        if not isinstance(name, str):
            raise TypeError("{Product name should be a string!")
        if not isinstance(price, (int, float)):
            raise TypeError("Price should be integer or float data type!")
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} {self.price}'


class Customer:
    __slots__ = ['name', 'surname', 'mobile']

    def __init__(self, name, surname, mobile):
        if not name or not surname or not mobile:
            raise ValueError("Missing values in input!")
        self.name = name
        self.surname = surname
        self.mobile = mobile

    def __str__(self):
        return f"\nName - {self.name}\nSurname - {self.surname}\nPhone number - {self.mobile}"


class Order:
    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Argument for order should be Customer type!")
        self.info = customer
        self.prod_list = []

    def add_item(self, product):
        if not isinstance(product, Product):
            raise TypeError("Argument for new item should be Product type!")
        self.prod_list.append(product)

    def checkout(self):
        total = sum([x.price for x in self.prod_list])
        return f'Customer info: {str(self.info)}' f'\nTotal for the order: {total} Items bought: {[str(x) for x in self.prod_list]} '


def main():
    john = Customer('Max', 'Terikhov', '03674859374')
    prod1 = Product('Apple', 7)
    prod2 = Product('Ginger', 5)
    ord = Order(john)
    ord.add_item(prod1)
    ord.add_item(prod2)
    print(ord.checkout())


if __name__ == '__main__':
    main()