class Person:
    """This is a new class called Person"""

    age = 15

    @staticmethod
    def greetings ():
        print('Hello everyone!')


print(Person.greetings())
print(Person.age)
print(Person.__doc__)

#Create a new object of Person class
matheus = Person()

print(matheus.age)

#Output: <bound method Person.greet of <__main__.Person object>>
print(matheus.greetings)
matheus.greetings()