contactos = {}

def agregar_contacto(nombre, numero):
    contactos[nombre] = numero
    print(f"Contacto '{nombre}' agregado.")

def buscar_contacto(nombre):
    if nombre in contactos:
        print(f"{nombre}: {contactos[nombre]}")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

#Metodo agregar_contacto
agregar_contacto("Ana", "123456789")
agregar_contacto("Carlos", "987654321")

#Metodo buscar_contacto
buscar_contacto("Ana")
buscar_contacto("Carlos")

#Metodo eliminar_contacto
eliminar_contacto("Carlos")

input("Teclee cualquier tecla...")