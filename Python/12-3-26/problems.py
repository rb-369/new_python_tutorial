# Problem: Vehicle Information System

# Design a program using inheritance.

# 🔹 Base Class: Vehicle

# Create a class Vehicle with the following attributes:

# vehicle_id

# brand

# price

# Methods:

# display_vehicle()

# Displays vehicle details.

# 🔹 Derived Class: Car (inherits from Vehicle)

# Add the following additional attributes:

# num_doors

# fuel_type

# Methods:

# display_car_details()

# Display all vehicle details along with car-specific information.

# 🔹 Tasks

# Create at least 2 car objects.

# Display their details.

# Example Output
# Vehicle ID: 201
# Brand: Toyota
# Price: 800000
# Doors: 4
# Fuel Type: Petrol
# 🟡 Moderate Level Problem
# Problem: Employee Salary Management System

# Create a program using inheritance to manage employee salaries.

# 🔹 Base Class: Employee
# Attributes

# emp_id

# name

# base_salary

# Methods

# display_employee()

# Display employee details.

# annual_salary()

# Return yearly salary:

# base_salary × 12
# 🔹 Derived Class: Manager

# Additional attributes:

# department

# bonus

# Methods

# total_salary()

# Calculate total annual salary:

# (base_salary × 12) + bonus

# display_manager()

# Display all manager details including department and total salary.

# 🔹 Tasks

# Create multiple manager objects.

# Store them in a list (array) of objects.

# Display all managers' details.

# 🎯 Concepts Practiced

# These problems cover:

# Class creation

# Object instantiation

# Single inheritance

# Method reuse

# Method extension in child class

# List (array) of objects

# ✅ If you want, I can also give:

# 🔥 Hard inheritance problem (3-level inheritance)

# 🔥 Student → UGStudent → PGStudent problem

# 🔥 Bank Account inheritance problem (very common in interviews)

# 🔥 DevOps-style inheritance problem (Server → WebServer → DatabaseServer).


#1)
class Vehicle:
    def __init__(self, v_id, v_brand, price):
        self.v_id=v_id
        self.v_brand=v_brand
        self.price=price

    def display_vehicle(self):
        print(f"Vehicle ID: {self.v_id}")  
        print(f"Vehicle Brand: {self.v_brand}")  
        print(f"Vehicle Price: {self.price}")  

class Car(Vehicle):
    def __init__(self, v_id:str, v_brand, price, num_doors, fuel_type):
        Vehicle.__init__(self,v_id, v_brand, price)
        self.num_doors = num_doors
        self.fuel_type=fuel_type

    def display_car(self):
        super().display_vehicle()
        print(f"No. of Doors: {self.num_doors}")           
        print(f"Fuel Type: {self.fuel_type}")

def main():
    v1 = Vehicle("l1", "Lambo", 100000)
    v1.display_vehicle()

    c1 = Car("C1", "Toyota", 20000, 4, "Petrol")
    c1.display_car()

if __name__ == '__main__':
    main()
    
