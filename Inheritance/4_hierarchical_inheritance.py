class Company:

    def __init__(self, company_name: str):
        self.company_name = company_name

    def company_info(self):
        return f"Company: {self.company_name}"


class Employee(Company):

    def __init__(self, employee_name: str, company_name: str):
        self.employee_name = employee_name
        self.company_name = company_name

    def employee_info(self):
        response = Company.company_info(self)
        print(f"Employee: {self.employee_name}, {response}")


class Manager(Company):

    def __init__(self, manager_name: str, company_name: str):
        self.manager_name = manager_name
        self.company_name = company_name

    def manager_info(self):
        response = Company.company_info(self)
        print(f"Manager: {self.manager_name}, {response}")


# Create objects
emp = Employee("Akhil", "Google")
mgr = Manager("Eshwar", "Google")

emp.employee_info()
print("-----")
mgr.manager_info()