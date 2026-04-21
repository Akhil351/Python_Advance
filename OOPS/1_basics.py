class Car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} car is starting.")

    def get_details(self):
        print(f"Brand: {self.brand}, Color: {self.color}")
        

car1=Car()
car2=Car()

car1.set_details("Toyota","Red")

car2.set_details("BMW","Black")

car1.start()
car1.get_details()

print("-------------------")

car2.start()
car2.get_details()



# Class (Car) → Design of a car 🚗
# Object (car1, car2) → Actual cars built from that design