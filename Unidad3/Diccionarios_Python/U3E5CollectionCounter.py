from collections import Counter

texto = "python java python c c c java"
frecuencia = Counter(texto.split())
print(frecuencia)

input("Teclee cualquier tecla...")