"""
Los obras de arte pueden ser ordenadas con cierto grado de objetividad según su
belleza. Un vendedor de cuadros descubrió que si ordenaba sus obras según este
criterio y posteriormente priorizaba la venta de los cuadros que tuviesen una
cantidad parecida de cuadros más feos y cuadros más lindos que ellos, entonces
sus ganancias mejorarían considerablemente. Sin embargo, no podemos siempre
considerar todos los cuadros porque ciertos clientes le solicitan que el cuadro
esté dentro de un rango de dimensiones. Se tomarán para la priorización cuadros
que tengan dimensiones iguales de cada lado o que a lo sumo tengan una
diferencia de 1. Se nos da una lista de cuadros determinados por: un
identificador único, su nivel de belleza, su altura y su ancho. Diseñar un
algoritmo que dada también las restricciones del cliente (máximo y mínimo para
altura y anchura), nos diga qué cuadro debería priorizar el vendedor.
"""

altura_minima = 5
altura_maxima = 7
anchura_minima = 5
anchura_maxima = 7

lista_cuadros = [
    ('cuadro1', 1, 1, 1),
    ('cuadro2', 2, 2, 2),
    ('cuadro3', 3, 3, 3),
    ('cuadro4', 4, 4, 4),
    ('cuadro5', 5, 5, 5),
    ('cuadro6', 6, 6, 6),
    ('cuadro7', 7, 7, 7),
    ('cuadro8', 8, 8, 8),
]

def cual_vender(lista_cuadros, altura_minima, altura_maxima, anchura_minima, anchura_maxima):
    return 0
