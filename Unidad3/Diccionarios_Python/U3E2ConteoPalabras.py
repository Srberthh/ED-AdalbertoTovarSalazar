texto = "hola mundo hola python mundo"

palabras = texto.split()
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)

input("Teclee cualquier opcion...")