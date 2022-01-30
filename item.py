import csv


class Item:
    pay_rate = 0.8 # Pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Price {quantity} is not greater than 0!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self) -> None:
        self.__price = self.__price * self.pay_rate

    def apply_increament(self, incre_value) -> None:
        self.__price = self.__price + self.__price * incre_value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        self.__name = value

    def calculateTotalPrice(self) -> int:
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls) -> None:
        with open('classesItemCSV.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                __name=item.get('name'),
                __price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num) -> bool:
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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    def __connect(self, smto_server) -> None:
        pass

    def __prepare_body(self) -> str:
        return f"""
        Hello Someone.
        we have {self.name} {self.quantity} times.
        """

    def __send(self) -> None:
        pass

    def send_email(self) -> None:
        self.__connect('')
        self.__prepare_body()
        self.__send()
