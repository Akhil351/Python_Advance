class Company:

    def info(self):
        print("This is a company")


class Employee(Company):

    def info(self):   # overriding
        print("This is an employee")


obj = Employee()
obj.info()


# 👉 Overriding = change parent method in child