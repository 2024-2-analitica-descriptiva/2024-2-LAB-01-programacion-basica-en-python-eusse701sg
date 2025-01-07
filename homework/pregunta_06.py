"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores_por_clave = {}
    with open("files/input/data.csv", 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  # Separar por tabulaciones
            diccionario_codificado = columnas[4]  # Quinta columna
            
            # Separar pares clave:valor
            pares = diccionario_codificado.split(',')
            for par in pares:
                clave, valor = par.split(':')
                valor = int(valor)
                
                if clave in valores_por_clave:
                    # Actualizar máximo y mínimo
                    valores_por_clave[clave]['max'] = max(valores_por_clave[clave]['max'], valor)
                    valores_por_clave[clave]['min'] = min(valores_por_clave[clave]['min'], valor)
                else:
                    # Inicializar con el primer valor
                    valores_por_clave[clave] = {'max': valor, 'min': valor}

    # Convertir a una lista de tuplas (clave, min, max) ordenadas alfabéticamente por la clave
    resultado = [(clave, datos['min'], datos['max']) for clave, datos in sorted(valores_por_clave.items())]
    return resultado

print(pregunta_06())
