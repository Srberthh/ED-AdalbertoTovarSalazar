import time
import random

def bubble_sort(lista):
    """Implementa Bubble Sort O(n²)"""
    arr = lista.copy()  # No modificar la lista original
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def merge_sort(lista):
    """Implementa Merge Sort O(n log n)"""
    if len(lista) <= 1:
        return lista.copy()
    
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    """Función auxiliar para merge_sort"""
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def medir_tiempo(algoritmo, lista):
    """Mide tiempo de ejecución de un algoritmo"""
    inicio = time.perf_counter()
    resultado = algoritmo(lista)
    fin = time.perf_counter()
    
    # Verificar que está ordenado correctamente
    assert resultado == sorted(lista), "Error: Lista no ordenada correctamente"
    
    return fin - inicio

# 2.1: Evaluación de Rendimiento por Dimensión
print("TABLA 2.1 - Tiempos de Ejecución por Dimensión")
print("=" * 60)
print(f"{'Dimensión':<10} {'Bubble Sort (s)':<15} {'Merge Sort (s)':<15} {'Relación BS/MS':<15}")
print("-" * 60)

dimensiones = [100, 500, 1000, 5000, 10000]

for dim in dimensiones:
    # Generar secuencia aleatoria de elementos únicos
    lista = random.sample(range(1, dim * 10), dim)
    
    # Medir tiempos
    tiempo_bubble = medir_tiempo(bubble_sort, lista)
    tiempo_merge = medir_tiempo(merge_sort, lista)
    
    # Calcular relación
    relacion = tiempo_bubble / tiempo_merge if tiempo_merge > 0 else 0
    
    print(f"{dim:<10,} {tiempo_bubble:<15.6f} {tiempo_merge:<15.6f} {relacion:<15.2f}")

print()

# 2.2: Análisis de Casos Específicos
print("TABLA 2.2 - Comportamiento en Casos Especificos (n=1000)")
print("=" * 70)
print(f"{'Escenario':<15} {'Bubble Sort (s)':<15} {'Merge Sort (s)':<15} {'Observaciones':<25}")
print("-" * 70)

# Casos específicos
casos = {
    "Ordenado": list(range(1000)),
    "Inverso": list(range(1000, 0, -1)),
    "Casi ordenado": [x if x % 100 != 0 else x + 500 for x in range(1000)]
}

observaciones = {
    "Ordenado": "Mejor caso BS",
    "Inverso": "Peor caso BS",
    "Casi ordenado": "Caso intermedio"
}

for nombre, lista in casos.items():
    tiempo_bubble = medir_tiempo(bubble_sort, lista)
    tiempo_merge = medir_tiempo(merge_sort, lista)
    obs = observaciones[nombre]
    
    print(f"{nombre:<15} {tiempo_bubble:<15.6f} {tiempo_merge:<15.6f} {obs:<25}")

print()
print("ANALISIS:")
print("- Bubble Sort: O(n²) - sensible al orden inicial")
print("- Merge Sort: O(n log n) - rendimiento consistente")
print("- Relación BS/MS aumenta exponencialmente con n")
input("Presione Enter para cerrar...")