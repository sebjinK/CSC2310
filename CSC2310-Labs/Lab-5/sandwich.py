# TITLE:    sandwich.PY
# AUTHOR:   SEBJIN KENNEDY
# DATE:     11/15/2023
# PURPOSE:  Bring about better understanding of python classes and subclasses

class Sandwich:
    def __init__(self, order_number, bread_type, meat_type):
        self._order_number = order_number
        self._bread_type = bread_type
        self._meat_type = meat_type
        self._toppings = []

    @property
    def order_number(self):
        return self._order_number

    @property
    def bread_type(self):
        return self._bread_type

    @property
    def meat_type(self):
        return self._meat_type

    def add_topping(self, topping):
        self._toppings.append(topping)

    def remove_topping(self, topping):
        if topping in self._toppings:
            self._toppings.remove(topping)

    @property
    def price(self):
        return 3.75 + 0.50 * len(self._toppings)

    def info(self):
        print(f"Order Number: {self.order_number}")
        print(f"Bread Type: {self.bread_type}")
        print(f"Meat Type: {self.meat_type}")
        print(f"Toppings: {', '.join(self._toppings)}")
        print(f"Price: ${self.price:.2f}")


class Meal(Sandwich):
    def __init__(self, order_number, bread_type, meat_type, drink, side):
        super().__init__(order_number, bread_type, meat_type)
        self._drink = drink
        self._side = side

    @property
    def drink(self):
        return self._drink

    @property
    def side(self):
        return self._side

    @property
    def price(self):
        return 6.75 + 0.50 * len(self._toppings)

    def info(self):
        super().info()
        print(f"Drink: {self.drink}")
        print(f"Side: {self.side}")


class KidsMeal(Meal):
    def __init__(self, order_number, bread_type, meat_type, drink, side, toy):
        super().__init__(order_number, bread_type, meat_type, drink, side)
        self._toy = toy

    @property
    def toy(self):
        return self._toy

    @property
    def price(self):
        return 4.75 + 0.30 * len(self._toppings)

    def info(self):
        super().info()
        print(f"Toy: {self.toy}")


# Example usage:
sandwich = Sandwich(order_number=1, bread_type="Wheat", meat_type="Turkey")

sandwich.info()

print("\n")

meal = Meal(order_number=2, bread_type="White", meat_type="Ham", drink="Soda", side="Chips")
sandwich.add_topping("Lettuce")
sandwich.add_topping("Tomato")
meal.info()

print("\n")

kids_meal = KidsMeal(order_number=3, bread_type="Italian", meat_type="Chicken",
                     drink="Potion of Regret", side="Apple Slices", toy="Buzz Lightyear")
kids_meal.add_topping("Pickles")
kids_meal.info()