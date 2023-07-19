#----------------------Ejercicio 2------------------

def filtrar_lista(lista):
    salida = []
    for numero in lista:
        if numero > 1000:
            break
        if numero % 5 == 0 and numero <= 600:
            salida.append(numero)
    return salida
#Se utiliza los ejemplos dados por los enunciados para validar funcionalidad

print(filtrar_lista([24, 150, 300, 660, 295, 1050,50])) #Output: [150, 300, 295]
print(filtrar_lista([110, 720, 307, 555, 1095, 12, 300, 1000])) #Output: [110, 555]
 