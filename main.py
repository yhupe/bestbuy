from products import Product
from store import Store

product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


def start(store):

    while True:

        print('''
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
        ''')
        print()
        user_input = input("Please choose a number: ")
        print()

        if user_input == "1":


        if user_input == "2":
            store.get_total_quantity()

        if user_input == "3":
            print(store.get_all_products())
            print()
            user_order_product = input("")
            user_order_quantity = input("")
            store.order(user_order_quantity)

        if user_input =="4":
            break

start(best_buy)

