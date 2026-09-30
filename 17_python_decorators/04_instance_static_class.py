class Employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def print_info(self):
        info= f"Then name is {self.name} and the salary is {self.salary}"
        print(info)

    @staticmethod
    def sum(a,b):
        # self.a=a
        # self.b=b
        return a+b

    @classmethod
    def print_comany(cls):
        print(cls.company)

    @classmethod
    def change_comany(cls,c2):
        cls.company=c2

e1=Employee("Jack", 3434)
e2=Employee("Jill",433)

print(Employee.company)
# print(Employee.name)

e1.print_info()
e2.print_info()

print(e2.sum(5,23))

e1.print_comany()
e1.change_comany("AWS")
print(Employee.company)
