class Car:
    
    wheels=4 # class variable
    
    def __init__(self,brand, color):
        self.brand=brand
        self.color=color
        
    # Instance method    
    def get_detials(self):
        print(f"Brand: {self.brand}, Color: {self.color}")
        
    # Class method
    @classmethod
    def get_wheels(cls):
        print(f"Number of wheels: {cls.wheels}")
        
    # 🔵 Static Method
    @staticmethod
    def general_info():
        print("Cars are used for transportation")
    
    
# Create object
car1 = Car("Toyota", "Red")

print("----- Car Details -----")
car1.get_detials()

print("\n----- Car Wheels -----")
Car.get_wheels()

print("\n----- General Info -----")
Car.general_info()



# | Type     | Think Like      | Example Question                |
# | -------- | --------------- | ------------------------------- |
# | Instance | One car 🚗      | “What is THIS car’s color?”     |
# | Class    | All cars 🚗🚗🚗 | “How many wheels do cars have?” |
# | Static   | General fact 🌍 | “What are cars used for?”       |


# 👉 Instance → one object
# 👉 Class → all objects
# 👉 Static → general utility


# 🎯 When to Use Each Method

# 🟢 1. Instance Method → when data is different per object
# 🟡 2. Class Method → when data is same for all objects
# 🔵 3. Static Method → when no object or class data is needed