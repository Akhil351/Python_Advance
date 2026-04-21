class Company:

    def info(self):
        print("This is a company")


class Employee(Company):

    def info(self):
        print("This is an employee")


class Manager(Company):

    def info(self):
        print("This is a manager")


# Create objects
c = Company()
e = Employee()
m = Manager()

c.info()
e.info()
m.info()

# 👉 Polymorphism = same method name behaving differently