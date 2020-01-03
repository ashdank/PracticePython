class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
blue = Dog("Blue", 10)

def max_ages(*args):
    return max (*args)

print "The oldest dog is " + str(max_ages(philo.age,mikey.age,blue.age)) + " years old"
