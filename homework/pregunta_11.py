"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    suma_por_letra = {}
    
    with open("files/input/data.csv", 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  # Separar por tabulaciones
            letra_col_4 = columnas[3]  # Cuarta columna (letras separadas por coma)
            valor_col_2 = int(columnas[1])  # Segunda columna (valor numérico)

            # Para cada letra en la columna 4, sumamos el valor de la columna 2
            for letra in letra_col_4.split(','):
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor_col_2
                else:
                    suma_por_letra[letra] = valor_col_2
    
    # Ordenar el diccionario por las claves alfabéticamente
    return dict(sorted(suma_por_letra.items()))

print(pregunta_11())