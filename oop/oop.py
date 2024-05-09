class Employee:
    def __init__(self,first,last,pay,):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last+ '@company.compile'

    def fullname(self):
        return '{}{}'.format(self.first,self.last)


Emp1 = Employee('max','pol',50000)
Emp2 = Employee('jack','will',60000)


#print(Emp1)
#print(Emp2)
print(Emp1.email)
print(Emp2.email)

print(Employee.fullname(Emp1))