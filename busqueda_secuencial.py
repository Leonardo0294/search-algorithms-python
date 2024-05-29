def busqueda_secuencial(lista, valor):
    posicion = 0
    encontrado = False

    while posicion < len(lista) and not encontrado:
        if lista[posicion] == valor:
            encontrado = True
        else:
            posicion += 1

    return encontrado, posicion

# Ejemplo de uso

numeros = [2, 7, 3, 5, 13, 31, 29, 17, 19]
llave = 37

encontrado, posicion = busqueda_secuencial(numeros, llave)

if encontrado:
    print(f"El valor {llave} se encuentra en la posición {posicion}")
else:
    print(f"El valor {llave} no se encuentra en la lista")
