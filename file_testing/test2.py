import numpy as np

def quantos_anos(soy_anos):
    print(f'Yo tengo {soy_anos} anos')

class Pero:

    def __init__(self, color):
        self.color = color

    def quieres(self):
        nonlocal self
        return self.color
pero_uno = Pero('rojo')
print(pero_uno.quieres())
familia = ['Taghi, Parastou, Arzhang']

def mi_familia(papa, mama, hermano):
    if papa in familia:
        print(f'Si! {papa} in mi familia')
    else:
        print(f'No! {papa} not in mi familia')
    if mama in familia and hermano not in familia:
        print(f'{mama} in mi familia. {hermano} from nada')
    elif hermano in familia and mama not in familia:
        return lambda x: print(mama)
    else:
        return False == True