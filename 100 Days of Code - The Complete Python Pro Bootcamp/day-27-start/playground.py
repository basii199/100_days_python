# use *args or **kwargs in function params to accept any number of values
# the names don't matter, just the number of stars.

# unlimited positional arguments - the position matters
# *args - arguments
# *args is of type list

def add(*args):
    total_sum = 0
    for arg in args:
        total_sum += arg
    return total_sum

# print(add(1,2,3,4,5,6,7,8,9))

# unlimited keyword arguments - you must pass named parameters
# **kwargs = keyword arguments
# kwargs is of type dict

def greet(**kwargs):
    print(f'Hello {kwargs["name"]} from {kwargs["address"]}')

# unused keywords are simply ignored
greet(name='Basi', address='Nigeria', any='any')

# works for classes too
class NewClassCar:
    def __init__(self, **kwargs):
        # use .get('') so it returns None instead of the program crashing
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')

car = NewClassCar(make='IDK')
print(car.make, car.model)