"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    asociaciones = {}
    with open("files/input/data.csv", 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  # Separar por tabulaciones
            letra = columnas[0]  # Primera columna (letra)
            valor_columna_2 = int(columnas[1])  # Segunda columna como entero
            
            if valor_columna_2 in asociaciones:
                asociaciones[valor_columna_2].add(letra)  # Usar set para eliminar duplicados
            else:
                asociaciones[valor_columna_2] = {letra}  # Inicializar con un set

    # Convertir los sets a listas, ordenar y luego convertir a tuplas
    resultado = [(valor, sorted(list(letras))) for valor, letras in sorted(asociaciones.items())]
    return resultado

print(pregunta_08())