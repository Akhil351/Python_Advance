# 👉 Pydantic is used to validate and structure data using Python classes
from pydantic import BaseModel, StrictInt


# -----------------------------
# 1. Basic Model
# -----------------------------
class EmployeeSchema(BaseModel):
    name: str
    id: int
    department: str


print("----- Basic Object -----")
obj = EmployeeSchema(name="John Doe", id=123, department="HR")
print(obj)


print("\n----- Using Dictionary (**kwargs) -----")
data = {"name": "John Doe", "id": 123, "department": "HR"}
obj2 = EmployeeSchema(**data)
print(obj2)


# -----------------------------
# 2. Coercion Example
# -----------------------------
print("\n----- Coercion Example -----")
# id is string but will be converted to int
obj3 = EmployeeSchema(**{"name": "John Doe", "id": "101", "department": "HR"})
print(obj3)


# -----------------------------
# 3. Strict Types Example
# -----------------------------
class EmployeeStrictSchema(BaseModel):
    name: str
    id: StrictInt
    department: str


print("\n----- Strict Type Example -----")
obj4 = EmployeeStrictSchema(**{"name": "John Doe", "id": 101, "department": "HR"})
print(obj4)


print("\n----- Strict Type Error Example -----")
try:
    # This will fail because id is string and StrictInt does NOT allow conversion
    obj5 = EmployeeStrictSchema(**{"name": "John Doe", "id": "101", "department": "HR"})
    print(obj5)
except Exception as e:
    print("Error:", e)