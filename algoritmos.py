import time

# Búsqueda Lineal
def busqueda_lineal(lista, valor):
    inicio = time.time()  # Guardar el tiempo de inicio
    for i in range(len(lista)):
        if lista[i] == valor:
            fin = time.time()  # Guardar el tiempo de finalización
            tiempo_ejecucion = fin - inicio  # Calcular el tiempo de ejecución
            return True, i, tiempo_ejecucion
    return False, -1, None

# Búsqueda Binaria
def busqueda_binaria(lista, valor):
    primero = 0
    ultimo = len(lista) - 1
    inicio = time.time()  # Guardar el tiempo de inicio

    while primero <= ultimo:
        medio = (primero + ultimo) // 2
        if lista[medio] == valor:
            fin = time.time()  # Guardar el tiempo de finalización
            tiempo_ejecucion = fin - inicio  # Calcular el tiempo de ejecución
            return True, medio, tiempo_ejecucion
        elif lista[medio] < valor:
            primero = medio + 1
        else:
            ultimo = medio - 1

    return False, -1, None

# Ejemplo de uso
numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
valor_busqueda = 23

# Búsqueda Lineal
encontrado_lineal, indice_lineal, tiempo_lineal = busqueda_lineal(numeros, valor_busqueda)
print("Búsqueda Lineal:")
print(f"¿Valor {valor_busqueda} encontrado? {encontrado_lineal}")
if encontrado_lineal:
    print(f"Índice del valor {valor_busqueda}: {indice_lineal}")
    print(f"Tiempo de ejecución: {tiempo_lineal} segundos")

# Búsqueda Binaria
encontrado_binaria, indice_binaria, tiempo_binaria = busqueda_binaria(numeros, valor_busqueda)
print("\nBúsqueda Binaria:")
print(f"¿Valor {valor_busqueda} encontrado? {encontrado_binaria}")
if encontrado_binaria:
    print(f"Índice del valor {valor_busqueda}: {indice_binaria}")
    print(f"Tiempo de ejecución: {tiempo_binaria} segundos")
