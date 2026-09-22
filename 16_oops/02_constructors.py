class Employee:
    company="HP"

    def __init__(self,salary,name,bond):

        self.salary=salary
        self.name=name
        self.bond=bond
        pass

    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name

e1 =Employee(34000,"John",3)

print(e1.get_salary())
print(e1.get_info())

