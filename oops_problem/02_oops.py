class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printPerson(self):
        print(f"the name of the person is {self.name} and the age is {self.age}")

p=Person("John",34)

print(p.name,p.age)

p2=Person.printPerson()

print(p2)