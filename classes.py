import csv



class Item:
    pay_rate = 0.8 # Pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Price {quantity} is not greater than 0!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculateTotalQuantity(self) -> int:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('classesItemCSV.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        # We will count out float that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out floats that are points zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

print(Item.is_integer(7.5))