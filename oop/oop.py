class Animal:
    def __init__(self, name):
        print('Animal named {} was born'.format(name))
        self.name = name

    @classmethod
    def specie(cls):
        print('General specie of class', cls)

    @staticmethod
    def is_animal(obj):
       print('Is', obj, 'instance of animal:', isinstance(obj, Animal))

Animal.specie()
Animal.is_animal('some string')

print()

a = Animal('ET')
a.specie()
Animal.is_animal(a)
a.is_animal(a)

print()

class Dog(Animal):
    years = 0
    tricks = []

    def __init__(self, name):
        super().__init__(name)
        self.bark()
        Dog.bark(self)

    def bark(self):
        print('{}: Haf'.format(self.name))

    @classmethod
    def specie(cls):
        print('Dog of class', cls)

rex = Dog('Rex')
rex.specie()

Animal.is_animal(rex)
Dog.is_animal(rex)
rex.is_animal(rex)

print('Is', a, 'of type Animal:', type(a) == Animal)
print('Is', rex, 'of type Animal:', type(rex) == Animal)
print('Is', a, 'of type Dog:', type(rex) == Dog)

fido = Dog('Fido')

print(fido.name, rex.name)
fido.name = 'Fidy'
print(fido.name, rex.name)

print(Dog.tricks, fido.tricks, rex.tricks)
fido.tricks.append('play dead')
print(Dog.tricks, fido.tricks, rex.tricks)  # Oops, trick should be instance variable

# But beware mutable vs imutable
print(Dog.years, fido.years, rex.years)
fido.years += 1
print(Dog.years, fido.years, rex.years)  # poor Fido
Dog.years += 2
print(Dog.years, fido.years, rex.years)  # poor Rex

fido.special = True
print()


class MagicObject:
    """Magic is happening here"""

    def __call__(self):
        print('called')

    def __str__(self):
        return 'sss'

    def __repr__(self):
        return 'MagicObject()'

m = MagicObject()
m()
print(m.__doc__)
print(str(m))
print(m)
print(repr(m))
