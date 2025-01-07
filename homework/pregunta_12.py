"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra = {}

    with open("files/input/data.csv", 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  # Separar por tabulaciones
            letra_col_1 = columnas[0]  # Primera columna (letra)
            columna_5 = columnas[4]  # Quinta columna (diccionario codificado como cadena)

            # Separar los pares clave:valor de la columna 5 y sumar los valores
            suma_columna_5 = sum(int(par.split(':')[1]) for par in columna_5.split(','))

            # Agregar la suma al diccionario por la letra de la columna 1
            if letra_col_1 in suma_por_letra:
                suma_por_letra[letra_col_1] += suma_columna_5
            else:
                suma_por_letra[letra_col_1] = suma_columna_5

    return suma_por_letra

print(pregunta_12())