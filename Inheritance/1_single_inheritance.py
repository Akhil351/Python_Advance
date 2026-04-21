class Company:
    def __init__(self, company_name: str):
        self.company_name = company_name

    def info(self):
        return f"Company Name: {self.company_name}"


class Employee(Company):
    def __init__(self,employee_name: str, company_name: str):
        self.employee_name=employee_name
        self.company_name=company_name
        
    def employe_info(self):
        company_response=Company.info(self)
        print(f"The Employee Name: {self.employee_name}, {company_response}")
        
        
obj=Employee("Akhil","Google")

obj.employe_info()


# 📚 Types of Inheritance
# 1. 🟢 Single Inheritance

# 👉 One parent → One child

# 2. 🟡 Multilevel Inheritance

# 👉 Grandparent → Parent → Child

# 3. 🔵 Multiple Inheritance

# 👉 Multiple parents → One child

# 4. 🟣 Hierarchical Inheritance

# 👉 One parent → Multiple children

# 5. 🟠 Hybrid Inheritance

# 👉 Combination of multiple types