def n_esimo_termino(numero, terminos):
    suma = 0
    for i in range(1, terminos + 1):
        suma += int(str(numero) * i)
    return suma

print(n_esimo_termino(3,5)) #Output= 37035

print(n_esimo_termino(5,3)) #Output = 615



