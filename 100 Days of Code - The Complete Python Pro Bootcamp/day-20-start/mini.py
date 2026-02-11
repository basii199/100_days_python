# learn inheritance

# syntax

# Inheritance
class Animal:
    def __init__(self):
         self.eyes = 2

    def breathe(self):
        print('Inhale, Exhale')

# Initialize the child class with the parent class.
class Fish(Animal):
    def __init__(self):
        # Use super().__init__() to initialize the parent's properties and methods
        super().__init__()

    def swim(self):
        print('Move in water')

    def breathe(self):
        # Call method on parent (super) to have all this parents functionality and add extra
        super().breathe()
        print('Doing this under water')

nemo = Fish()

nemo.swim()
nemo.breathe()

