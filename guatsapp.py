"""
Debido a la popularidad de la aplicación de mensajería “GuatsApp”, se nos pide
realizar un algoritmo que determine el grado de amistad entre cada par de
usuarios y los ordene de mayor a menor. Tenemos un listado de mensajes definidos
como (string remitente, string destinatario, string texto). El grado de amistad
será la suma de la cantidad de caracteres en el historial de conversación de un
par de usuarios. Si nunca hablaron su grado de amistad es 0.

1. Determinar grado de amistad entre cada par de usuarios.
2. Ordenar de mayor a menor.
"""

mensajes = [
    ('agus', 'jorge', 'hola! todo bien?'),
    ('pedro', 'juan', 'bien y tu?'),
    ('pedro', 'matias', 'buen dia matias!!'),
    ('juan', 'pedro', 'hola como andas?'),
]

def mejores_amigos(mensajes):
    amistades = set_amistades(mensajes)
    amistades = ordenar(amistades)
    string = 'Amigos: %s - %s \n' \
             'Grado de Amistad: %d' \
              % (amistades[0][0], amistades[0][1], amistades[0][2])
    return string

def set_amistades(mensajes):
    amistades = []
    for mensaje in mensajes:
        usuario1 = mensaje[0]
        usuario2 = mensaje[1]
        texto = mensaje[2]
        amistades = grado_amistad(usuario1, usuario2, amistades, texto)
    return amistades

def grado_amistad(usuario1, usuario2, amistades, texto):
    grado = len(texto)
    exist = False
    for amistad in amistades:
        if usuario1 in amistad and usuario2 in amistad:
            amistad[2] += grado
            exist = True
            break
    if not exist:
        amistades.append([usuario1, usuario2, grado])
    return amistades

def ordenar(amistades):
    ordenar = True
    while (ordenar):
        ordenar = False
        for i in range(1, len(amistades)):
            if amistades[i][2] > amistades[i-1][2]:
                aux = amistades[i-1]
                amistades[i-1] = amistades[i]
                amistades[i] = aux
                ordenar = True
    return amistades

print (mejores_amigos(mensajes))
