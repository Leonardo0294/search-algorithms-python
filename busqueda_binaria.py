def busqueda_binaria(lista, valor):
    """
    Función que implementa el algoritmo de búsqueda binaria para encontrar un valor en una lista ordenada.

    Argumentos:
        lista: La lista ordenada en la que se busca el valor.
        valor: El valor que se busca en la lista.

    Retorno:
        True si el valor se encuentra en la lista, False en caso contrario.
    """

    primero = 0
    ultimo = len(lista) - 1
    encontrado = False

    while primero <= ultimo and not encontrado:
        mitad = (primero + ultimo) // 2

        if lista[mitad] == valor:
            encontrado = True
        else:
            if valor < lista[mitad]:
                ultimo = mitad - 1
            else:
                primero = mitad + 1

    return encontrado


# Ejemplo de uso

numeros = [2, 3, 5, 7, 11, 13, 17, 19]
llave = 10

resultado = busqueda_binaria(numeros, llave)

if resultado:
    print(f"El valor {llave} se encuentra en la lista.")
else:
    print(f"El valor {llave} no se encuentra en la lista.")
