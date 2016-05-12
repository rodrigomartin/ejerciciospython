"""
Un grupo de científicos está analizando una forma de vida inteligente extraterrestre
en la reconocida área 52. Han descubierto que, sorprendentemente, estos usan las mismas
letras que nosotros (26 letras, excluyendo la ñ) aunque su alfabeto posee un orden distinto.
Se nos encomienda la tarea de reordenar un diccionario en español para que los extraterrestres
puedan buscar palabras en nuestra lengua más fácilmente. Diseñar un algoritmo que dada un
string que representa todas las letras del alfabeto ordenadas según los extraterrestres y una
lista de palabras, devuelva una lista de palabras ordenadas (en el orden que entiendan los
extraterrestres)
"""

# ordenada = ['revestir', 'miel', 'extraterrestre', 'auto', 'automovil', 'al']

lista = ['miel', 'extraterrestre', 'al', 'automovil', 'auto', 'revestir']
alfabeto = 'zyxwvutsrqponmlkjihgfedcba'

def ordenar_extraterrestre(lista, alfabeto):
    ordenada = lista
    listo = False
    while (listo == False):
        listo = True
        for i in range(1, len(ordenada)):
            palabra1 = ordenada[i-1]
            palabra2 = ordenada[i]
            orden = determina_orden(palabra1, palabra2, alfabeto)

            if orden[0] != palabra1 and orden[1] != palabra2:
                ordenada[i-1] = orden[0]
                ordenada[i] = orden[1]
                listo = False
    return ordenada

def determina_orden(palabra1, palabra2, alfabeto):
    orden = [palabra1, palabra2]
    largo1 = len(palabra1)
    largo2 = len(palabra2)

    for i in range(0, largo1):
        if i == largo2:
            orden = [palabra2, palabra1]
            break

        letra1 = palabra1[i]
        letra2 = palabra2[i]
        pos1 = alfabeto.find(letra1)
        pos2 = alfabeto.find(letra2)

        if pos1 < pos2:
            orden = [palabra1, palabra2]
            break
        elif pos2 < pos1:
            orden = [palabra2, palabra1]
            break

    return orden

lista = ordenar_extraterrestre(lista, alfabeto)
print(lista)
