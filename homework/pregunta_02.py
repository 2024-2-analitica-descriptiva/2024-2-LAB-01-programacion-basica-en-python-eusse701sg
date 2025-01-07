"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    conteo = {}
    with open("files/input/data.csv", 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  # Separar por tabulaciones
            letra = columnas[0]  # Obtener la letra de la primera columna
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1

    # Ordenar las letras alfabéticamente y convertir a una lista de tuplas
    resultado = sorted(conteo.items())
    return resultado

print(pregunta_02())