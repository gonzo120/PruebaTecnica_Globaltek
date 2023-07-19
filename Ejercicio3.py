#------------Ejercicio 3-----------------------------
def agruparElementos(lista):
    grupos = {}
    for elemento in lista:
        if elemento not in grupos:
            grupos[elemento] = []
        grupos[elemento].append(elemento)
    salida = []
    for grupo in grupos.values():
        salida.append(grupo)
    return salida


print(agruparElementos([12, 25, 1, 1, 7, 25])) #Output: [[12], [25, 25], [1, 1], [7]]
print(agruparElementos([6, 7, 8, 9])) #Output: [[6], [7], [8], [9]]


