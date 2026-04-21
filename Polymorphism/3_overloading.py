class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


obj = Calculator()

print(obj.add(2, 3))        # 2 values
print(obj.add(2, 3, 4))     # 3 values


# 👉 Overloading = same method handles different inputs