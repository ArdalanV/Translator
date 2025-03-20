importar numpy as np

def quantos_anos(soy_anos):
    imprimir(f"Yo tengo {soy_anos} anos")

clase Pero:

    def __inic__(yo, color):
        yo.color = color

    def quieres(yo):
        nolocal yo
        retornar yo.color


pero_uno = Pero("rojo")
imprimir(pero_uno.quieres())


familia = ["Taghi, Parastou, Arzhang"]

def mi_familia(papa, mama, hermano):
    si papa en familia:
        imprimir(f"Si! {papa} en mi familia")
    sino:
        imprimir(f"No! {papa} no en mi familia")
    si mama en familia y hermano no en familia:
        imprimir(f"{mama} en mi familia. {hermano} de nada")
    sino_si hermano en familia y mama no en familia:
        retornar lambda x : imprimir(mama)
    sino:
        retornar Falso == Verdadero
