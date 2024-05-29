import time

# Implementación de la búsqueda lineal
def linear_search(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Implementación de la búsqueda binaria
def binary_search(lista, objetivo):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == objetivo:
            return mid
        elif lista[mid] < objetivo:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Crear datos de prueba
datos = list(range(1000000))  # Lista grande ordenada
objetivo = 999999  # Valor a buscar

# Medir tiempo de ejecución de la búsqueda lineal
inicio = time.time()
indice_lineal = linear_search(datos, objetivo)
fin = time.time()
tiempo_lineal = fin - inicio
print(f"Linear Search: Index {indice_lineal}, Time {tiempo_lineal:.10f} seconds")

# Medir tiempo de ejecución de la búsqueda binaria
inicio = time.time()
indice_binaria = binary_search(datos, objetivo)
fin = time.time()
tiempo_binaria = fin - inicio
print(f"Binary Search: Index {indice_binaria}, Time {tiempo_binaria:.10f} seconds")

# Resultados
print(f"Linear Search took {tiempo_lineal:.10f} seconds")
print(f"Binary Search took {tiempo_binaria:.10f} seconds")
