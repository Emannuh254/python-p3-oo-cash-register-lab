class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize the CashRegister with an optional discount.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        """
        Add items to the register.
        :param title: Name of the item.
        :param price: Price per item.
        :param quantity: Number of items.
        """
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        """
        Apply the discount to the total if available and print the appropriate message.
        """
        if self.discount:
            self.total *= (1 - self.discount / 100)
            self.total = round(self.total, 2)  # Ensure the total is rounded
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Void the last transaction by subtracting it from the total.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0  # Reset last transaction amount
