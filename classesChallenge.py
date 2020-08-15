# class

class Cat:
    # class variable
    catInfo = 'I guess cats and lions might be related'

    # class function
    def meow(self):
        print('the cat MEOW ')


myCat = Cat()
myCat.meow()
# adding instance variables
myCat.jump = 'cats jump a lot'
myCat.milk = 'this cat likes milk'
print(myCat.milk)

# otherCat = Cat()
# print(otherCat.milk)
# will throw error

# access to class variable anywhere
print(Cat.catInfo)
# modify class info
Cat.catInfo = 'cats and lions are felines'
print(Cat.catInfo)


# this class initializes class variables
class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


# must give value to class variables
# myDog = Dog()
# will throw error
myDog = Dog('fido', 10, 'brown')
print(f'my dog age is ', myDog.age)


# this class has default values
class Wolf:

    def __init__(self, name=' ', age=0, color='unknown color'):
        self.name = name
        self.age = age
        self.color = color


myWolf = Wolf()
print(myWolf.color)


# this class also has another function


class Fox:

    def __init__(self, name=' ', age=0, color='orange'):
        self.name = name
        self.age = age
        self.color = color

    def chase(self, other_animal):
        print('the fox chases ' + other_animal)


wildFox = Fox()
wildFox.chase('rabbits.')
# challenge: Add a method to the Car class called age that returns how old the car is (2020 - year)


class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        old = 2020 - self.year
        print('Age of the car : ', old)


mySeventiesCar = Car(1970, 'ford', 'mustang')
mySeventiesCar.age()
