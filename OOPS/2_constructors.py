class Car:
    wheels=4
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} car is starting.")

    def get_details(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Wheels: {Car.wheels}")


car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")


car1.start()
car1.get_details()

print("-------------------")

car2.start()
car2.get_details()



# 👉 Constructor is used to automatically initialize an object’s data when it is created.

# without parameters → called default constructor
# with parameters → called parameterized constructor