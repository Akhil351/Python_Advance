class Company:

    def __init__(self, company_name: str):
        self.company_name = company_name

    def company_info(self):
        return f"Company: {self.company_name}"


class Manager(Company):

    def __init__(self, manager_name: str, company_name: str):
        self.manager_name = manager_name
        self.company_name = company_name

    def manager_info(self):
        response = Company.company_info(self) # or super().company_info()
        return f"Manager: {self.manager_name}, {response}"


class Employee(Manager):

    def __init__(self, employee_name: str, manager_name: str, company_name: str):
        self.employee_name = employee_name
        self.manager_name = manager_name
        self.company_name = company_name

    def employee_info(self):
        response = Manager.manager_info(self)
        print(f"Employee: {self.employee_name}, {response}")


# Create object
obj = Employee("Akhil", "Eshwar", "Google")
obj.employee_info()