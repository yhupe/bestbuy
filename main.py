from products import Product
from store import Store


def main():
    """ Main function that runs the store application. """

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = Store(product_list)

    iphone = Product("Iphone 15 Pro 256 GB", price=1099, quantity=1000)
    cannabis = Product("1st grade PREMIUM Cannabis", price=20, quantity=50)

    best_buy.add_product(iphone)
    best_buy.add_product(cannabis)
    best_buy.remove_product(cannabis)

    while True:
        print("\n     Menu     ")
        print(10 * " - ")
        print('''
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
        ''')
        print(10 * " - ")
        user_input = input("Please choose a number: ").strip()
        print()

        if user_input == "1":
            for index, product in enumerate(best_buy.get_all_products()):
                print(f"{index + 1}: {product.show()}")
            print()

        elif user_input == "2":
            print(f"Total amount of {best_buy.get_total_quantity()} items in store\n")

        elif user_input == "3":
            best_buy.process_order()

        elif user_input == "4":
            break


if __name__ == "__main__":
    main()
