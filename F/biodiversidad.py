import array as arr
from functools import reduce

especies = {
    "Rana Cristal": ("animal", 5, "rio"),
    "Murcielago de Nectar": ("animal", 2, "bosque"),
    "Trigrillo": ("animal", 3, "bosque"),
    "Mono Tití": ("animal", 6, "bosque"),
    "Palo e Mango": ("planta", 20, "rio"),
    "Palo Borracho": ("planta", 15, "rio"),
    "Tabaco": ("planta", 10, "bosque"),
    "Árbol de Caucho": ("planta", 5, "bosque"),
}

def actualizar_cantidad(especies, nombre, cantidad):
    return {**especies, nombre: (especies[nombre][0], cantidad, especies[nombre][2])}

def cambiar_habitat(especies, nombre, habitat):
    return {**especies, nombre: (especies[nombre][0], especies[nombre][1], habitat)}

def especies_tipo(especies, tipo):
    return list(filter(lambda nombre: especies[nombre][0] == tipo, especies))

def total_individuos(especies):
    return reduce(lambda acc, nombre: acc + especies[nombre][1], especies, 0)

def cantidades(especies):
    return arr.array('i', list(map(lambda nombre: especies[nombre][1], especies)))

def promedio(quantity):
    return reduce(lambda acc, x: acc + x, quantity) / len(quantity)

def formato_especies(especies):
    return "\n".join(map(lambda especie: f"{especie}: {especies[especie]}", especies))

# Ejemplo de uso
if __name__ == "__main__":
    print("------------------------")
    # Diccionario con formato
    print("Diccionario Original:\n")
    print(formato_especies(especies))
    print("------------------------")
    # Actualizar cantidad de individuos
    print("Cambio de Cantidad de Ranas Cristal:\n")
    especies = actualizar_cantidad(especies, "Rana Cristal", 10)
    print(formato_especies(especies))
    print("------------------------")
    # Cambiar habitat de una especie
    print("Cambio de Habitat de Rana Cristal:\n")
    especies = cambiar_habitat(especies, "Rana Cristal", "bosque")
    print(formato_especies(especies))
    print("------------------------")
    # Especies de un tipo
    print("Separación de especies por tipo:\n")
    print("Animales:")
    print(especies_tipo(especies, "animal"))
    print("Plantas:")
    print(especies_tipo(especies, "planta"))
    print("------------------------")
    # Total de individuos
    print("Total de Individuos observados:\n")
    print(total_individuos(especies))
    print("------------------------")
    # Arreglos de cantidades
    print("Arreglo de Cantidades:")
    quantities = cantidades(especies)
    print(quantities)
    print("")
    print("Promedio de Individuos:")
    print(promedio(quantities))