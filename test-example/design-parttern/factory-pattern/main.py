from abc import ABC, abstractmethod

from pizza import NYStyleCheesePizza, NYStylePepperoniPizza, NYStyleClamPizza, NYStyleVeggiePizza


class PizzaStore(ABC):
    @abstractmethod
    def orderPizza(self, pizza_type: str):
        pass

    @abstractmethod
    def createPizza(self, pizza_type: str):
        pass


class NYStylePizzaStore(PizzaStore):

    def orderPizza(self, pizza_type: str):
        pizza = self.createPizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    def createPizza(self, pizza_type: str):
        pizza = None

        if pizza_type == "cheese":
            pizza = NYStyleCheesePizza()
        elif pizza_type == "pepperoni":
            pizza = NYStylePepperoniPizza()
        elif pizza_type == "clam":
            pizza = NYStyleClamPizza()
        elif pizza_type == "veggie":
            pizza = NYStyleVeggiePizza()

        return pizza


nyPizzaStore = NYStylePizzaStore()
ordered_pizza = nyPizzaStore.orderPizza("cheese")
print()
print(f"Ordered a {ordered_pizza.get_name()}")
