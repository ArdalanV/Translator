importar math
importar os

# Una función simple para saludar a un usuario
def saludar_usuario(nombre):
    imprimir(f'Hello, {nombre}! Welcome to the program.')

def funcion_simple(hermano: entero) -> entero:
    si hermano y (not hermano):
        si 3 o (True y False):
            retornar hermano

# Una función para calcular el área de un círculo
def calcular_area_circulo(radio):
    si radio <= 0:
        imprimir('Invalid radius. Radius must be greater than 0.')
        retornar Ninguno
    retornar math.pi * radio ** 2

# Una función para leer un archivo y contar sus líneas
def contar_lineas_en_archivo(ruta_archivo):
    intentar:
        con abrir(ruta_archivo, 'r') como archivo:
            lineas = archivo.readlines()
            imprimir(f"The file '{ruta_archivo}' has {longitud(lineas)} lines.")
            retornar longitud(lineas)
    excepto FileNotFoundError:
        imprimir(f"Error: The file '{ruta_archivo}' was no found.")
        retornar 0

# Una clase que representa una calculadora básica
clase Calculadora:

    def __inic__(yo):
        yo.historial = []

    def sumar(yo, a, b):
        resultado = a + b
        yo.historial.append(f'Added {a} y {b}: {resultado}')
        retornar resultado

    def restar(yo, a, b):
        resultado = a - b
        yo.historial.append(f'Subtracted {b} de {a}: {resultado}')
        retornar resultado

    def multiplicar(yo, a, b):
        resultado = a * b
        yo.historial.append(f'Multiplied {a} y {b}: {resultado}')
        retornar resultado

    def dividir(yo, a, b):
        si b == 0:
            imprimir('Error: Division by zero es no allowed.')
            retornar Ninguno
        resultado = a / b
        yo.historial.append(f'Divided {a} by {b}: {resultado}')
        retornar resultado

    def mostrar_historial(yo):
        imprimir('Calculation History:')
        para registro en yo.historial:
            imprimir(registro)

def contador_sumador(a):
    b = 20

    def ayudante():
        nolocal b
        b = 14
        retornar lambda x: 20 si x == Verdadero sino 10
    retornar ayudante
valor = contador_sumador(10)()(True)
si __name__ == '__main__':
    saludar_usuario('Alice')
    radio = 5
    area = calcular_area_circulo(radio)
    si area:
        imprimir(f'The area of a circle con radius {radio} es {area:.2f}')
    ruta_archivo = 'example.txt'
    contar_lineas_en_archivo(ruta_archivo)
    calc = Calculadora()
    imprimir(calc.sumar(10, 5))
    imprimir(calc.restar(10, 5))
    imprimir(calc.multiplicar(10, 5))
    imprimir(calc.dividir(10, 0))
    calc.mostrar_historial()