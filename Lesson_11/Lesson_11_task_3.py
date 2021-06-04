class Product:
    """ Создание продукта """
    def __init__(self, type: str, name: str, price: float):
        self.type = type
        self.name = name
        self.price = price


product1 = Product('vegetable', 'potato', 2.65)
product2 = Product('vegetables', 'tomato', 5.50)
product3 = Product('fruit', 'banana', 7.30)
product4 = Product('fruit', 'apple', 4.75)


class ProductStore:
    money = 0
    stock = []

    """ Добавление продуктоктов в склад """
    def add(self, product, amount: int):
        product.price *= 1.30
        self.stock.append({'Product': product, 'Amount': amount})
        print(f'{amount} {product.name} was added!')

    """ Скидка на продукт """
    def set_discount(self, identifier: str, percent: str):  # Не виконана одна умова identifier_type
        percent_conversion = '1.' + percent.rstrip('%')
        float(percent_conversion)
        for i in self.stock:
            if identifier == i['Product'].name:
                i['Product'].price /= percent_conversion
                print(f'The discount {percent_conversion} was set for such products {identifier}')
            else:
                print('Something went wrong!')

    """ Продажа продукта """
    def sell_product(self, product_name: str, amount: int):
        for i in self.stock:
            if i['Product'].name == product_name:
                if i['Amount'] < amount:
                    print('Not enough product in stock!')
                else:
                    i['Amount'] -= amount
                    self.money += (amount * i['Product'].price)
            else:
                print('Something went wrong!')

    def get_income(self):
        print(self.money)

    def get_all_products(self):
        if len(self.stock) <= 0:
            print('Not enough product in stock!')
        else:
            for x in self.stock:
                print(x['Product'].type, x['Product'].name, x['Product'].price)

    def get_product_info(self, product_name: str):
        if len(self.stock) <= 0:
            print('Not enough product in stock!')
        else:
            for i in self.stock:
                if product_name == i['Product'].name:
                    prod_info = (i['Product'].name, i['Amount'])
                    print(prod_info)


product_store = ProductStore()


def user_interface():
    while True:
        print("""
1 - add product
2 - set discount
3 - sell product
4 - get income
5 - get all products
6 - get products info
q - quit
""")
        user_choice = input('Enter your action: ')
        if user_choice == '1':
            print(f'{product1.name}, {product2.name}, {product3.name}, {product4.name}')
            the_product_choice = input('Choose a product(write name a product): ')
            if the_product_choice == 'potato':
                product_store.add(product1, int(input('Enter quantity: ')))
            elif the_product_choice == 'tomato':
                product_store.add(product2, int(input('Enter quantity: ')))
            elif the_product_choice == 'banana':
                product_store.add(product3, int(input('Enter quantity: ')))
            elif the_product_choice == 'apple':
                product_store.add(product4, int(input('Enter quantity: ')))
            else:
                print('Something went wrong!')
        elif user_choice == '2':
            product_store.set_discount(input('Choose a product(write name a product): '),
                                       input('Enter discount percent: '))
        elif user_choice == '3':
            sell_choice = input('Choose a product: ')
            product_store.sell_product(sell_choice, int(input('Enter quantity: ')))
        elif user_choice == '4':
            product_store.get_income()
        elif user_choice == '5':
            product_store.get_all_products()
        elif user_choice == '6':
            product_store.get_product_info(input('Enter product name: '))
        elif user_choice == 'q':
            print('Bye!')
            break
        else:
            print('Something went wrong!')


user_interface()
