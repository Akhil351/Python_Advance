from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal


# -----------------------------
# 1. Define Model
# -----------------------------
class EmployeeSchema(BaseModel):

    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., gt=18, lt=65)
    email: EmailStr = Field(..., description="Employee's email address")
    department: Optional[str] = None
    gender: Literal['Male', 'Female', 'Other'] = Field(..., description="Employee's gender")


# -----------------------------
# 2. Create Object (Direct)
# -----------------------------
print("----- Direct Object -----")
obj = EmployeeSchema(
    name="John Doe",
    age=30,
    email="john.doe@example.com",
    department="IT",
    gender="Male"
)
print(obj)


# -----------------------------
# 3. Create Object using **data
# -----------------------------
print("\n----- Using **data -----")
data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "department": "IT",
    "gender": "Male"
}

obj2 = EmployeeSchema(**data)
print(obj2)


# -----------------------------
# 4. Validation Error Example
# -----------------------------
print("\n----- Validation Error Example -----")
try:
    obj3 = EmployeeSchema(
        name="Jo",                 # too short
        age=17,                   # invalid
        email="invalid-email",    # wrong format
        gender="Male"
    )
    print(obj3)
except Exception as e:
    print("Error:", e)