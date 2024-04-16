import random

class Potion:
    def __init__(self, ingredient1, ingredient2):
        self.ingredients = [ingredient1, ingredient2]
    def get_name(self):
        if self.ingredients[0] == self.ingredients[1]:
            return "Failed Decoction"
        elif "Vampire's Breath" in self.ingredients or "Witch's Tongue" in self.ingredients:
            return "Elixir of Halitosis"
        elif "Toe of Frog" in self.ingredients or "Eye of Newt" in self.ingredients:
            return "Philter of Amphibiosity"
        elif "Adder's Fork" in self.ingredients or "Elephant's Proboscis" in self.ingredients:
            return "Draught of Eavesdropping"
        elif "Milk" in self.ingredients or "Marinara Sauce" in self.ingredients:
            return "Potion of Regret"
        else:
            return "Failed Decoction"
    def get_value(self):
        if self.get_name() == "Failed Decoction":
            return 1
        elif self.get_name() == "Elixir of Halitosis":
            return random.randint(10, 50)
        elif self.get_name() == "Philter of Amphibiosity":
            return random.randint(750, 1000)
        elif self.get_name() == "Draught of Eavesdropping":
            return random.randint(500, 750)
        elif self.get_name() == "Potion of Regret":
            return random.randint(2, 40)
      