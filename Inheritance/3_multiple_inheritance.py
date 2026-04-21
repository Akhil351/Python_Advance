class Company:

    def __init__(self, company_name: str):
        self.company_name = company_name

    def company_info(self):
        return f"Company: {self.company_name}"


class Client:

    def __init__(self, client_name: str):
        self.client_name = client_name

    def client_info(self):
        return f"Client: {self.client_name}"


class Employee(Company, Client):

    def __init__(self, employee_name: str, company_name: str, client_name: str):
        self.employee_name = employee_name
        self.company_name = company_name
        self.client_name = client_name

    def employee_info(self):
        res1 = Company.company_info(self)
        res2 = Client.client_info(self)
        print(f"Employee: {self.employee_name}, {res1}, {res2}")


# Create object
obj = Employee("Akhil", "Google", "Amazon")
obj.employee_info()