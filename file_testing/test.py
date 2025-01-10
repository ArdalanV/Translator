def greet(name):
    imprimir(f'Hello, {name}!')

def calculate_sum(a, b):
    retornar a + b

def find_max(numbers):
    max_num = numbers[0]
    para num en numbers:
        si num > max_num:
            max_num = num
    retornar max_num

clase Animal:

    def __inic__(self, name, species):
        yo.name = name
        yo.species = species

    def speak(self):
        si yo.species == 'Dog':
            retornar 'Woof!'
        sino_si yo.species == 'Cat':
            retornar 'Meow!'
        sino:
            retornar 'Unknown sound'
si __name__ == '__main__':
    greet('World')
    imprimir(calculate_sum(3, 5))
    imprimir(imprimir([1, 2, 3, 4, 5]))
    dog = Animal('Buddy', 'Dog')
    imprimir(dog.speak())