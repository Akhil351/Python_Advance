# Python Advanced Concepts - Learning Repository

A comprehensive collection of Python advanced programming concepts with practical examples. This repository covers Object-Oriented Programming (OOP), Inheritance, Polymorphism, Decorators, Async Programming, MultiThreading, and Pydantic data validation.

## Table of Contents

- [Overview](#overview)
- [Topics Covered](#topics-covered)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Detailed Topics](#detailed-topics)
  - [Object-Oriented Programming (OOP)](#1-object-oriented-programming-oop)
  - [Inheritance](#2-inheritance)
  - [Polymorphism](#3-polymorphism)
  - [Decorators](#4-decorators)
  - [Async Programming](#5-async-programming)
  - [MultiThreading](#6-multithreading)
  - [Pydantic](#7-pydantic)
- [Running Examples](#running-examples)
- [Learning Path](#learning-path)
- [Best Practices](#best-practices)
- [Resources](#resources)
- [Contributing](#contributing)

## Overview

This repository serves as a practical guide to advanced Python programming concepts. Each topic includes:
- Clear, concise code examples
- Inline comments explaining key concepts
- Real-world analogies for better understanding
- Progressive difficulty levels

**Target Audience**: Python developers looking to master advanced concepts and improve their coding skills.

## Topics Covered

### 1. Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Encapsulation (Public, Protected, Private)
- Methods (Instance, Class, Static)

### 2. Inheritance
- Single Inheritance
- Multilevel Inheritance
- Multiple Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance

### 3. Polymorphism
- Method Overriding
- Operator Overloading
- Duck Typing

### 4. Decorators
- Function Decorators
- Wrapper Functions
- Adding Functionality

### 5. Async Programming
- Async/Await Syntax
- Concurrent Task Execution
- asyncio.gather()
- Non-blocking I/O Operations

### 6. MultiThreading
- ThreadPoolExecutor
- Concurrent Task Execution
- Thread Management

### 7. Pydantic
- Data Validation
- Type Checking
- Field Constraints
- Model Serialization
- Email Validation

## Prerequisites

- **Python**: 3.8 or higher
- **Basic Python Knowledge**: Variables, functions, loops, conditionals
- **Understanding of**: Functions, classes (basic)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Python_Advance
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# For Pydantic examples
pip install pydantic[email]

# Or install all dependencies at once
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python main.py
```

Expected output:
```
Hello from python-advance!
```

## Project Structure

```
Python_Advance/
├── main.py                              # Entry point
│
├── OOPS/                                # Object-Oriented Programming
│   ├── 1_basics.py                      # Classes & Objects
│   ├── 2_constructors.py                # __init__ method
│   ├── 3_encapulsation.py               # Public, Protected, Private
│   └── 4_methods.py                     # Instance, Class, Static methods
│
├── Inheritance/                         # Inheritance Concepts
│   ├── 1_single_inheritance.py          # Parent → Child
│   ├── 2_multilevel_inhertiance.py      # Grandparent → Parent → Child
│   ├── 3_multiple_inheritance.py        # Multiple Parents → Child
│   ├── 4_hierarchical_inheritance.py    # Parent → Multiple Children
│   └── 5_hybrid_inheritance.py          # Combination of types
│
├── Polymorphism/                        # Polymorphism Concepts
│   ├── 1_polymorphism.py                # Method Overriding
│   ├── 2_overriding.py                  # Override Parent Methods
│   └── 3_overloading.py                 # Operator Overloading
│
├── Decorator/                           # Decorator Pattern
│   ├── 1_decorator.py                   # Basic Decorator
│   └── 2_decorator.py                   # Advanced Decorators
│
├── Async/                               # Asynchronous Programming
│   ├── 1_basic.py                       # Basic async/await
│   └── 2_multiple_task.py               # Concurrent tasks
│
├── MultiThreading/                      # Concurrent Execution
│   ├── 1_multithreading.py              # Basic threading
│   └── 2_multithreading.py              # ThreadPoolExecutor
│
└── Pydantic/                            # Data Validation
    ├── 1_basics.py                      # BaseModel & Validation
    ├── 2_fields.py                      # Field Constraints
    └── 3_serialization.py               # Model Serialization
```

## Detailed Topics

## 1. Object-Oriented Programming (OOP)

### 1.1 Classes and Objects (`OOPS/1_basics.py`)

**Concept**: A class is a blueprint, and an object is an instance created from that blueprint.

```python
class Car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color
    
    def start(self):
        print(f"{self.brand} car is starting.")
    
    def get_details(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

# Create objects
car1 = Car()
car1.set_details("Toyota", "Red")
car1.start()  # Output: Toyota car is starting.
```

**Real-World Analogy**:
- **Class** (Car) → Design of a car 🚗
- **Object** (car1, car2) → Actual cars built from that design

### 1.2 Constructors (`OOPS/2_constructors.py`)

**Concept**: Constructors automatically initialize an object's data when it's created.

```python
class Car:
    wheels = 4  # Class variable
    
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
```

**Key Points**:
- `__init__` is called automatically when object is created
- `self` refers to the current object
- **Default constructor**: No parameters
- **Parameterized constructor**: With parameters

### 1.3 Encapsulation (`OOPS/3_encapulsation.py`)

**Concept**: Protect data and control how it's accessed.

```python
class BankAccount:
    def __init__(self, name, age, balance):
        self.name = name              # Public
        self._age = age               # Protected
        self.__balance = balance      # Private
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

acc = BankAccount("Akhil", 22, 1000)
print(acc.name)           # ✅ Public - accessible
print(acc._age)           # ⚠️ Protected - should only use in class/subclass
# print(acc.__balance)    # ❌ Private - not accessible
print(acc.get_balance())  # ✅ Use method to access private data
```

**Access Levels**:
- `public` → Everyone can use
- `_protected` → Only class + child classes should use
- `__private` → Only inside the class

### 1.4 Methods (`OOPS/4_methods.py`)

**Concept**: Three types of methods based on what they access.

```python
class Car:
    wheels = 4  # Class variable
    
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    # Instance method - accesses instance data
    def get_details(self):
        print(f"Brand: {self.brand}, Color: {self.color}")
    
    # Class method - accesses class data
    @classmethod
    def get_wheels(cls):
        print(f"Number of wheels: {cls.wheels}")
    
    # Static method - doesn't access any data
    @staticmethod
    def general_info():
        print("Cars are used for transportation")
```

**Comparison Table**:

| Type     | Think Like      | Example Question                | Access         |
|----------|-----------------|--------------------------------|----------------|
| Instance | One car 🚗      | "What is THIS car's color?"    | `self`         |
| Class    | All cars 🚗🚗🚗 | "How many wheels do cars have?"| `cls`          |
| Static   | General fact 🌍 | "What are cars used for?"      | None           |

**When to Use**:
- 🟢 **Instance Method** → When data is different per object
- 🟡 **Class Method** → When data is same for all objects
- 🔵 **Static Method** → When no object or class data is needed

## 2. Inheritance

### 2.1 Single Inheritance (`Inheritance/1_single_inheritance.py`)

**Concept**: One parent → One child

```python
class Company:
    def __init__(self, company_name):
        self.company_name = company_name
    
    def info(self):
        return f"Company Name: {self.company_name}"

class Employee(Company):
    def __init__(self, employee_name, company_name):
        self.employee_name = employee_name
        self.company_name = company_name
    
    def employee_info(self):
        company_response = Company.info(self)
        print(f"Employee: {self.employee_name}, {company_response}")

obj = Employee("Akhil", "Google")
obj.employee_info()
# Output: Employee: Akhil, Company Name: Google
```

### 2.2 Multilevel Inheritance (`Inheritance/2_multilevel_inhertiance.py`)

**Concept**: Grandparent → Parent → Child

```python
class Company:
    def company_info(self):
        return f"Company: {self.company_name}"

class Manager(Company):
    def manager_info(self):
        response = super().company_info()
        return f"Manager: {self.manager_name}, {response}"

class Employee(Manager):
    def employee_info(self):
        response = Manager.manager_info(self)
        print(f"Employee: {self.employee_name}, {response}")
```

**Structure**:
```
Company (Grandparent)
   ↓
Manager (Parent)
   ↓
Employee (Child)
```

### 2.3 Multiple Inheritance (`Inheritance/3_multiple_inheritance.py`)

**Concept**: Multiple parents → One child

```python
class Company:
    def company_info(self):
        return f"Company: {self.company_name}"

class Client:
    def client_info(self):
        return f"Client: {self.client_name}"

class Employee(Company, Client):
    def __init__(self, employee_name, company_name, client_name):
        self.employee_name = employee_name
        self.company_name = company_name
        self.client_name = client_name
    
    def employee_info(self):
        res1 = Company.company_info(self)
        res2 = Client.client_info(self)
        print(f"Employee: {self.employee_name}, {res1}, {res2}")
```

**Structure**:
```
  Company    Client
      \      /
       \    /
      Employee
```

### 2.4 Hierarchical Inheritance (`Inheritance/4_hierarchical_inheritance.py`)

**Concept**: One parent → Multiple children

**Structure**:
```
      Company
     /   |   \
    /    |    \
 Emp1  Emp2  Emp3
```

### 2.5 Hybrid Inheritance (`Inheritance/5_hybrid_inheritance.py`)

**Concept**: Combination of multiple types of inheritance

## 3. Polymorphism

### 3.1 Method Overriding (`Polymorphism/1_polymorphism.py`)

**Concept**: Same method name behaving differently in different classes.

```python
class Company:
    def info(self):
        print("This is a company")

class Employee(Company):
    def info(self):
        print("This is an employee")

class Manager(Company):
    def info(self):
        print("This is a manager")

c = Company()
e = Employee()
m = Manager()

c.info()  # Output: This is a company
e.info()  # Output: This is an employee
m.info()  # Output: This is a manager
```

**Key Point**: Same method name (`info()`), different behavior.

### 3.2 Operator Overloading (`Polymorphism/3_overloading.py`)

**Concept**: Define how operators work with custom classes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__
print(p3)  # Output: Point(4, 6)
```

## 4. Decorators

### 4.1 Basic Decorator (`Decorator/1_decorator.py`)

**Concept**: Add extra functionality to a function without modifying its original code.

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
# Output:
# Before function
# Hello
# After function
```

**Real-World Analogy**: Decorating a gift 🎁 - the gift is the same, but you add wrapping paper.

**Common Uses**:
- Logging
- Authentication
- Performance timing
- Caching

## 5. Async Programming

### 5.1 Basic Async (`Async/1_basic.py`)

**Concept**: Run tasks without blocking, improving performance for I/O operations.

```python
import asyncio

async def download_file(file_name, delay):
    print(f"Starting download: {file_name}")
    await asyncio.sleep(delay)
    print(f"Finished download: {file_name}")
    return f"{file_name} downloaded"

async def main():
    results = await asyncio.gather(
        download_file("file1.pdf", 2),
        download_file("file2.jpg", 3),
        download_file("file3.mp4", 1)
    )
    print("All downloads completed.")

asyncio.run(main())
```

**Output**:
```
Starting download: file1.pdf
Starting download: file2.jpg
Starting download: file3.mp4
Finished download: file3.mp4
Finished download: file1.pdf
Finished download: file2.jpg
All downloads completed.
```

### 5.2 Multiple Tasks (`Async/2_multiple_task.py`)

**Concept**: Execute multiple async tasks concurrently.

```python
async def api_call():
    print("Fetching API data...")
    await asyncio.sleep(3)
    print("API data fetched")

async def process_data():
    print("Processing data...")
    await asyncio.sleep(5)
    print("Data processed")

async def save_data():
    print("Saving data...")
    await asyncio.sleep(2)
    print("Data saved")

async def main():
    await asyncio.gather(
        api_call(),
        process_data(),
        save_data()
    )
    print("All tasks completed.")
```

### Async vs MultiThreading

**🧍 Async (Single person multitasking)**:
- One person:
  - Starts cooking 🍳
  - While waiting → checks phone 📱
  - While waiting → does another task
- **Smart waiting**

**👨‍👩‍👦 MultiThreading (Multiple people)**:
- 3 people:
  - One cooks 🍳
  - One cleans 🧹
  - One shops 🛒
- **Work happens truly in parallel**

**Key Difference**: In async, when one task waits (`await`), other tasks continue running.

## 6. MultiThreading

### 6.1 ThreadPoolExecutor (`MultiThreading/1_multithreading.py`)

**Concept**: Run multiple tasks concurrently using a pool of threads.

```python
from concurrent.futures import ThreadPoolExecutor

def task(name):
    print(f"Task {name} is running")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(task, "A")
    executor.submit(task, "B")
    executor.submit(task, "C")
```

**Output** (order may vary):
```
Task A is running
Task B is running
Task C is running
```

**Use Cases**:
- CPU-intensive tasks
- True parallel execution
- I/O operations that don't support async

## 7. Pydantic

### 7.1 Basic Model (`Pydantic/1_basics.py`)

**Concept**: Validate and structure data using Python classes.

```python
from pydantic import BaseModel, StrictInt

class EmployeeSchema(BaseModel):
    name: str
    id: int
    department: str

# Create object
obj = EmployeeSchema(name="John Doe", id=123, department="HR")
print(obj)
# Output: name='John Doe' id=123 department='HR'

# Using dictionary
data = {"name": "John Doe", "id": 123, "department": "HR"}
obj2 = EmployeeSchema(**data)
```

**Type Coercion**:
```python
# id is string but will be converted to int
obj3 = EmployeeSchema(name="John Doe", id="101", department="HR")
print(obj3)  # Works! id="101" → id=101
```

**Strict Types**:
```python
class EmployeeStrictSchema(BaseModel):
    name: str
    id: StrictInt  # No conversion allowed
    department: str

# This will FAIL
obj = EmployeeStrictSchema(name="John", id="101", department="HR")
# Error: Input should be a valid integer
```

### 7.2 Field Validation (`Pydantic/2_fields.py`)

**Concept**: Add constraints and validation rules to fields.

```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

class EmployeeSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., gt=18, lt=65)
    email: EmailStr
    department: Optional[str] = None
    gender: Literal['Male', 'Female', 'Other']

# Valid object
obj = EmployeeSchema(
    name="John Doe",
    age=30,
    email="john.doe@example.com",
    department="IT",
    gender="Male"
)

# Invalid object - will raise ValidationError
try:
    obj = EmployeeSchema(
        name="Jo",                 # Too short (min_length=3)
        age=17,                    # Too young (gt=18)
        email="invalid-email",     # Wrong format
        gender="Male"
    )
except Exception as e:
    print("Validation Error:", e)
```

**Field Constraints**:
- `min_length`, `max_length` - String length
- `gt`, `lt`, `ge`, `le` - Number comparisons
- `EmailStr` - Email validation
- `Literal` - Allowed values only
- `Optional` - Can be None

### 7.3 Model Serialization (`Pydantic/3_serialization.py`)

**Concept**: Convert models to/from dictionaries and JSON.

```python
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age: int
    email: str

# Create from dict
data = {"name": "John", "age": 30, "email": "john@example.com"}
emp = Employee(**data)

# Convert to dict
print(emp.model_dump())
# Output: {'name': 'John', 'age': 30, 'email': 'john@example.com'}

# Convert to JSON
print(emp.model_dump_json())
# Output: '{"name":"John","age":30,"email":"john@example.com"}'
```

## Running Examples

### Run Individual Files

```bash
# OOP Examples
python OOPS/1_basics.py
python OOPS/2_constructors.py
python OOPS/3_encapulsation.py
python OOPS/4_methods.py

# Inheritance Examples
python Inheritance/1_single_inheritance.py
python Inheritance/2_multilevel_inhertiance.py
python Inheritance/3_multiple_inheritance.py

# Polymorphism Examples
python Polymorphism/1_polymorphism.py

# Decorator Examples
python Decorator/1_decorator.py

# Async Examples
python Async/1_basic.py
python Async/2_multiple_task.py

# MultiThreading Examples
python MultiThreading/1_multithreading.py

# Pydantic Examples
python Pydantic/1_basics.py
python Pydantic/2_fields.py
python Pydantic/3_serialization.py
```

### Run All Examples

```bash
# Create a script to run all examples
python run_all_examples.py
```

## Learning Path

### Beginner Level
1. **Start with OOP Basics** (`OOPS/1_basics.py`)
2. **Learn Constructors** (`OOPS/2_constructors.py`)
3. **Understand Encapsulation** (`OOPS/3_encapulsation.py`)
4. **Master Methods** (`OOPS/4_methods.py`)

### Intermediate Level
5. **Single Inheritance** (`Inheritance/1_single_inheritance.py`)
6. **Multilevel Inheritance** (`Inheritance/2_multilevel_inhertiance.py`)
7. **Multiple Inheritance** (`Inheritance/3_multiple_inheritance.py`)
8. **Polymorphism** (`Polymorphism/1_polymorphism.py`)
9. **Decorators** (`Decorator/1_decorator.py`)

### Advanced Level
10. **Async Programming** (`Async/1_basic.py`, `Async/2_multiple_task.py`)
11. **MultiThreading** (`MultiThreading/1_multithreading.py`)
12. **Pydantic Validation** (`Pydantic/1_basics.py`, `Pydantic/2_fields.py`)

### Recommended Order:
```
OOP → Inheritance → Polymorphism → Decorators → Async/Threading → Pydantic
```

## Best Practices

### 1. OOP Best Practices
- Use meaningful class and method names
- Keep classes focused (Single Responsibility Principle)
- Use encapsulation to protect data
- Prefer composition over inheritance when possible

### 2. Async Programming Best Practices
- Use async for I/O-bound operations
- Always await async functions
- Use `asyncio.gather()` for concurrent tasks
- Handle exceptions properly in async functions

### 3. Threading Best Practices
- Use threading for CPU-bound tasks
- Limit number of threads with `max_workers`
- Clean up resources properly
- Be aware of GIL (Global Interpreter Lock) in Python

### 4. Pydantic Best Practices
- Define clear validation rules
- Use type hints consistently
- Handle validation errors gracefully
- Use `Optional` for nullable fields
- Leverage `Field` for detailed constraints

## Common Patterns

### Factory Pattern
```python
class Animal:
    @staticmethod
    def create(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
```

### Singleton Pattern
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Observer Pattern (with Decorators)
```python
def notify(func):
    def wrapper(*args, **kwargs):
        print(f"Notifying observers...")
        result = func(*args, **kwargs)
        print(f"Notification complete")
        return result
    return wrapper
```

## Resources

### Official Documentation
- [Python OOP Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Threading Documentation](https://docs.python.org/3/library/threading.html)

### Additional Learning
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- [Real Python - Async](https://realpython.com/async-io-python/)
- [Python Decorators Explained](https://realpython.com/primer-on-python-decorators/)

## Troubleshooting

### Common Issues

**1. Import Error with Pydantic**
```bash
# Install with email support
pip install pydantic[email]
```

**2. Async Not Running**
```python
# Always use asyncio.run() for main async function
asyncio.run(main())
```

**3. Inheritance Confusion**
```python
# Use super() to call parent methods
class Child(Parent):
    def __init__(self):
        super().__init__()  # Call parent constructor
```

## Contributing

Contributions are welcome! Feel free to:
1. Add new examples
2. Improve documentation
3. Fix bugs
4. Suggest new topics

### How to Contribute
1. Fork the repository
2. Create a feature branch
3. Add your examples with clear comments
4. Update README if needed
5. Submit a pull request

## Future Topics

Planned additions:
- [ ] Context Managers
- [ ] Generators and Iterators
- [ ] Metaclasses
- [ ] Abstract Base Classes
- [ ] Property Decorators
- [ ] Type Hints (Advanced)
- [ ] Design Patterns
- [ ] Testing with pytest

## License

This project is licensed under the MIT License.

## Acknowledgments

- Python Software Foundation for excellent documentation
- Pydantic team for amazing data validation library
- Python community for best practices and patterns

## Contact

For questions or suggestions:
- Create an issue on GitHub
- Email: akhil.vathaluru@gmail.com

---

**Happy Learning! 🐍✨**

**Built with ❤️ by Akhileswar**
