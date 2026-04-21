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
# 2. Create Object
# -----------------------------
print("----- Object -----")
obj = EmployeeSchema(
    name="John Doe",
    age=30,
    email="john.doe@example.com",
    department="IT",
    gender="Male"
)

print(obj)


# -----------------------------
# 3. Serialization (dict)
# -----------------------------
print("\n----- model_dump() -----")
data_dict = obj.model_dump()
print(data_dict)


# -----------------------------
# 4. Serialization (JSON)
# -----------------------------
print("\n----- model_dump_json() -----")
data_json = obj.model_dump_json()
print(data_json)