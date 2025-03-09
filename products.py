class Product:
    """ Represents a product with a name, price, and quantity.
    The product becomes inactive when its quantity reaches zero. """

    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name:
            raise ValueError("Product name must be a non-empty string.")

        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0


    def get_quantity(self) -> int:
        """Returns the current quantity of the product. """

        return self.quantity


    def set_quantity(self, quantity):
        """Reduces the product's quantity and deactivates it if it reaches zero. """

        self.quantity -= quantity
        if self.quantity <= 0:
            self.deactivate()


    def is_active(self) -> bool:
        """Returns whether the product is active (i.e., available for purchase)."""

        return self.active

    def activate(self):
        """ Activates the product. """

        self.active = True


    def deactivate(self):
        """Deactivates the product."""

        self.active = False


    def show(self) -> str:
        """Returns a string representation of the product."""

        return f"{self.name}, Price: {self.price} €, Quantity: {self.quantity} pcs"


    def buy(self, quantity) -> float:
        """Processes the purchase of a product of the passed quantity. """
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        total_price = quantity * self.price
        self.set_quantity(quantity)
        return total_price
