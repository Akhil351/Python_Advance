class BankAccount:
    def __init__(self, name, age, balance):
        self.name = name
        self._age = age  # protected variable
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdraw successfully.")
        else:
            print("insufficent balance")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Akhil", 22, 1000)

acc.deposit(500)

acc.withdraw(400)

print(f"Current balance: {acc.get_balance()}")

print(f"Account holder: {acc.name}, Age: {acc._age}")

# ❌ Direct access not allowed
# print(acc.__balance)


# 👉 Encapsulation is used to protect data and control how it is used.
# 👉 Don’t allow direct access to data — use methods to control it


# public → everyone can use
# _protected → only class + child class should use
# __private → only inside the class