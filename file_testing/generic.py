"""
A sample Python script for testing code translation.
Includes classes, functions, loops, conditionals, and built-in functions.
"""

import math
import os

# A simple function to greet a user
def greet_user(name):
    print(f"Hello, {name}! Welcome to the program.")

def simple_function(brother: int) -> int:
    if brother and not brother:
        if 3 or True and False:
            return brother

# A function to calculate the area of a circle
def calculate_circle_area(radius):
    if radius <= 0:
        print("Invalid radius. Radius must be greater than 0.")
        return None
    return math.pi * radius ** 2

# A function to read a file and count its lines
def count_lines_in_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            print(f"The file '{file_path}' has {len(lines)} lines.")
            return len(lines)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0

# A class representing a basic calculator
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"Added {a} and {b}: {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"Subtracted {b} from {a}: {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"Multiplied {a} and {b}: {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return None
        result = a / b
        self.history.append(f"Divided {a} by {b}: {result}")
        return result

    def show_history(self):
        print("Calculation History:")
        for record in self.history:
            print(record)

def count_adder(a):
    b = 20
    def helper():
        nonlocal b
        b = 14
        return lambda x : 20 if x == True else 10
    return helper

val = count_adder(10)()(True)

# Main execution block
if __name__ == "__main__":
    greet_user("Alice")

    # Calculate the area of a circle
    radius = 5
    area = calculate_circle_area(radius)
    if area:
        print(f"The area of a circle with radius {radius} is {area:.2f}")

    # File handling example
    file_path = "example.txt"
    count_lines_in_file(file_path)

    # Using the Calculator class
    calc = Calculator()
    print(calc.add(10, 5))
    print(calc.subtract(10, 5))
    print(calc.multiply(10, 5))
    print(calc.divide(10, 0))  # Test division by zero
    calc.show_history()

