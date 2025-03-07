"""
A sample Python script para testing code translation.
Includes classes, functions, loops, conditionals, y built-in functions.
"""
importar math
importar os

def greet_user(name):
    imprimir(f'Hello, {name}! Welcome to the program.')

def calculate_circle_area(radius):
    si radius <= 0:
        imprimir('Invalid radius. Radius must be greater than 0.')
        retornar Ninguno
    retornar math.pi * radius ** 2

def count_lines_in_file(file_path):
    intentar:
        con abrir(file_path, 'r') como file:
            lines = file.readlines()
            imprimir(f"The file '{file_path}' has {longitud(lines)} lines.")
            retornar longitud(lines)
    excepto FileNotFoundError:
        imprimir(f"Error: The file '{file_path}' was no found.")
        retornar 0

clase Calculator:

    def __inic__(yo):
        yo.history = []

    def add(yo, a, b):
        result = a + b
        yo.history.append(f'Added {a} y {b}: {result}')
        retornar result

    def subtract(yo, a, b):
        result = a - b
        yo.history.append(f'Subtracted {b} de {a}: {result}')
        retornar result

    def multiply(yo, a, b):
        result = a * b
        yo.history.append(f'Multiplied {a} y {b}: {result}')
        retornar result

    def divide(yo, a, b):
        si b == 0:
            imprimir('Error: Division by zero es no allowed.')
            retornar Ninguno
        result = a / b
        yo.history.append(f'Divided {a} by {b}: {result}')
        retornar result

    def show_history(yo):
        imprimir('Calculation History:')
        para record en yo.history:
            imprimir(record)

def count_adder(a):
    b = 20

    def helper():
        nolocal b
        b = 14
        retornar lambda x: 20 si x == Verdadero sino 10
    retornar helper
val = count_adder(10)()(True)
si __name__ == '__main__':
    greet_user('Alice')
    radius = 5
    area = calculate_circle_area(radius)
    si area:
        imprimir(f'The area of a circle con radius {radius} es {area:.2f}')
    file_path = 'example.txt'
    count_lines_in_file(file_path)
    calc = Calculator()
    imprimir(calc.add(10, 5))
    imprimir(calc.subtract(10, 5))
    imprimir(calc.multiply(10, 5))
    imprimir(calc.divide(10, 0))
    calc.show_history()