"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    resultados = []
    with open("files/input/data.csv", 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  # Separar por tabulaciones
            letra = columnas[0]  # Primera columna (letra)
            columna_4 = columnas[3]  # Cuarta columna (lista de elementos separados por coma)
            columna_5 = columnas[4]  # Quinta columna (diccionario codificado como cadena)

            # Contar la cantidad de elementos en las columnas 4 y 5
            elementos_col_4 = len(columna_4.split(','))
            elementos_col_5 = len(columna_5.split(','))

            # Agregar la tupla con la letra y las cantidades
            resultados.append((letra, elementos_col_4, elementos_col_5))
    return resultados
print(pregunta_10())