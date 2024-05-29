import time
import timeit

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

# Funciones envoltorio para usar con timeit
def linear_search_wrapper():
    return linear_search(datos, objetivo)

def binary_search_wrapper():
    return binary_search(datos, objetivo)

# Medir tiempo de ejecución de la búsqueda lineal
tiempo_lineal = timeit.timeit(linear_search_wrapper, number=1)
indice_lineal = linear_search(datos, objetivo)
print(f"Linear Search: Index {indice_lineal}, Time {tiempo_lineal:.10f} seconds")

# Medir tiempo de ejecución de la búsqueda binaria
tiempo_binaria = timeit.timeit(binary_search_wrapper, number=1)
indice_binaria = binary_search(datos, objetivo)
print(f"Binary Search: Index {indice_binaria}, Time {tiempo_binaria:.10f} seconds")

# Resultados
print(f"Linear Search took {tiempo_lineal:.10f} seconds")
print(f"Binary Search took {tiempo_binaria:.10f} seconds")
