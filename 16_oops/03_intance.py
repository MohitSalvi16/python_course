class Employee:
    company="HP"

    def __init__(self,salary,name,bond,company):

        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company


    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name


e1=Employee(34999,"John",5,"Tesla")

print(e1.company)

print(dir(e1))

print(Employee.company)