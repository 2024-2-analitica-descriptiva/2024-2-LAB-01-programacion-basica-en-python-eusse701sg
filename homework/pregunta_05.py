"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores_por_letra = {}
    with open("files/input/data.csv", 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  # Separar por tabulaciones
            letra = columnas[0]  # Primera columna
            valor = int(columnas[1])  # Segunda columna como entero

            if letra in valores_por_letra:
                # Actualizar máximo y mínimo
                valores_por_letra[letra]['max'] = max(valores_por_letra[letra]['max'], valor)
                valores_por_letra[letra]['min'] = min(valores_por_letra[letra]['min'], valor)
            else:
                # Inicializar con el primer valor
                valores_por_letra[letra] = {'max': valor, 'min': valor}

    # Convertir a una lista de tuplas (letra, max, min) ordenadas alfabéticamente
    resultado = [(letra, datos['max'], datos['min']) for letra, datos in sorted(valores_por_letra.items())]
    return resultado

print(pregunta_05())