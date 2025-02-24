class Product:

    def __init__(self, name, price, quantity):

        if not name:
            raise ValueError("Name cannot be empty")
        if price <= 0:
            raise ValueError("Price cannot be negative or 0")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price} €, Quantity: {self.quantity} pcs")

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = quantity * self.price
        self.set_quantity(quantity)

        return total_price

