# *args - unlimited POSITIONAL arguments
# **kwargs - unlimited KEY WORD arguments

def add(*numbers):
    # numbers is a tuple with every argument passed is positional
    total = 0
    for num in numbers:
        total += num
    return total

# total = add(1, 2, 3, 4, 5, 2, 1, 1, 34, 0, 5)
# print(total)


def calculate(**kwargs):
    # kwargs is a dictionary with "add" as key and 23 as it's value
    print(kwargs.get("divisions"))
    # accessing the key with the get method - returns None is key does not exist


# calculate(add=23, multiply=45, division=26)


# example of using kwargs in a class
class Car:
    def __init__(self, **kwargs):
        self.model = "Toyota"
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


car = Car(seats=6)
print(car.seats)