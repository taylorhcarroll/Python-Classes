'''
1. Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.
2. Add a method for interacting with a pizza's toppings, called add_topping.
3. Add a method for outputting a description of the pizza (sample output below).
4. Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.
meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()
5.You should produce output in the terminal similiar to the following string.
"I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."
'''


class Pizza:
    def __init__(self):
        self.gluten_free = False
        self.size = ""
        self.crust_size = ""
        self.style = ""
        self.toppings = []
        self.order_name = ""

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        order = f'{self.order_name} would like a {self.crust_size}-inch{" gluten-free " if self.gluten_free else ""} {self.style} style pizza with '
        for topping in self.toppings:
            order += f'{topping}, '
        else:
            order = order[slice(-2)] + f'.'
        print(order)


dominos = Pizza()
dominos.crust_size = 12
dominos.order_name = "Taylor"
dominos.gluten_free = True
dominos.style = 'stuffed crust'
dominos.add_topping("chicken")
dominos.add_topping("black olive")
dominos.add_topping("red onion")

dominos.print_order()
