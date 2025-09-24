import time
import random

def busqueda_lineal(lista, objetivo):
    """
    Implementa búsqueda lineal O(n)
    Retorna posición del elemento o -1 si no existe
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    """
    Implementa búsqueda binaria O(log n)
    PRECONDICIÓN: lista debe estar ordenada
    """
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] > objetivo:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    
    return -1

# Pruebas de rendimiento
tamanos = [1000, 10000, 50000, 100000]

print(f"{'Tamaño':<10} {'Búsqueda Lineal (s)':<20} {'Búsqueda Binaria (s)':<22} {'Ratio':<10}")
print("-" * 65)

for tamano in tamanos:
    # 1. Generar lista ordenada
    lista = sorted(random.sample(range(1, tamano * 10), tamano))
    
    # 2. Elementos para buscar (5 existentes, 5 no existentes)
    elementos_existentes = random.sample(lista, 5)
    elementos_no_existentes = [max(lista) + i for i in range(1, 6)]
    elementos_prueba = elementos_existentes + elementos_no_existentes
    
    # 3. Medir tiempo búsqueda lineal
    inicio = time.perf_counter()
    for elemento in elementos_prueba:
        busqueda_lineal(lista, elemento)
    tiempo_lineal = (time.perf_counter() - inicio) / 10
    
    # 4. Medir tiempo búsqueda binaria
    inicio = time.perf_counter()
    for elemento in elementos_prueba:
        busqueda_binaria(lista, elemento)
    tiempo_binaria = (time.perf_counter() - inicio) / 10
    
    # 5. Calcular ratio
    ratio = tiempo_lineal / tiempo_binaria
    
    print(f"{tamano:<10,} {tiempo_lineal:<20.8f} {tiempo_binaria:<22.8f} {ratio:<10.2f}")

input("Presione Enter para cerrar...")