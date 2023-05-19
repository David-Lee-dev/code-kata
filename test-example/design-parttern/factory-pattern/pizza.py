from abc import ABC


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: list

    @classmethod
    def prepare(cls):
        print(f"Preparing {cls.name}")
        print(f"Tossing {cls.dough}...")
        print(f"Adding {cls.sauce}...")
        print(f"Adding toppings: ")
        for topping in cls.toppings:
            print(f"    {topping}")

    @classmethod
    def bake(cls):
        print("Bake for 25 minutes at 350")

    @classmethod
    def cut(cls):
        print("Cutting the pizza into diagonal slices")

    @classmethod
    def box(cls):
        print("Place pizza in official PizzaStore box")

    @classmethod
    def get_name(cls):
        return cls.name


class NYStyleCheesePizza(Pizza):
    name = "NY Style Sauce and Cheese Pizza"
    dough = "Thin Crust Dough"
    sauce = "Marinara Sauce"
    toppings = ["Grated Reggiano Cheese"]


class NYStylePepperoniPizza(Pizza):
    name = "NY Style Pepperoni Pizza"
    dough = "Thin Crust Dough"
    sauce = "Marinara Sauce"
    toppings = ["Grated Reggiano Cheese", "Sliced Pepperoni", "Garlic", "Onion", "Mushrooms", "Red Pepper"]


class NYStyleClamPizza(Pizza):
    name = "NY Style Clam Pizza"
    dough = "Thin Crust Dough"
    sauce = "Marinara Sauce"
    toppings = ["Grated Reggiano Cheese", "Fresh Clams from Long Island Sound"]


class NYStyleVeggiePizza(Pizza):
    name = "NY Style Veggie Pizza"
    dough = "Thin Crust Dough"
    sauce = "Marinara Sauce"
    toppings = ["Grated Reggiano Cheese", "Garlic", "Onion", "Mushrooms", "Red Pepper"]
