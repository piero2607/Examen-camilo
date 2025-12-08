from modules.lunarcristal import LunarCrystal
from modules.utils import *
datos_cristales = [
        {"nombre": "Eclipse", "energia": 82.5, "categorias": ["arcano", "nocturno"]},
        {"nombre": "Luna Llena", "energia": 95.0, "categorias": ["luminoso", "poderoso"]},
        {"nombre": "Cuarto Menguante", "energia": 35.2, "categorias": ["místico", "protector"]},
        {"nombre": "Aurora Lunar", "energia": 67.8, "categorias": ["energético", "sanador"]},
        {"nombre": "Estelar", "energia": 42.3, "categorias": ["cosmico", "visionario"]},
        {"nombre": "", "energia": 50.0, "categorias": ["test"]},  # Error: nombre vacío
        {"nombre": "Invalido", "energia": 150.0, "categorias": ["test"]},  # Error: > 100
        {"nombre": "SinCategorias", "energia": 30.0, "categorias": []},  # Error: lista vacía
        {"nombre": "Repetido", "energia": 60.0, "categorias": ["a", "a"]},  # Error: repetidas
    ]
cristales=[]
for dato in datos_cristales:
    try:
            cristal=LunarCrystal(
                nombre=dato["nombre"],
                energia_lunar=dato["energia"],
                categorias=dato["categorias"]
            )
            cristales.append(cristal)
    except ValueError as e:
        print("Error al crear " ,e)

print("ordenados de mayor a menor energia")
ordenados=ordenar_cristales_mayor_energia(cristales)
for o in ordenados:
    print("los cristales ordenados por energia: " ,o)

print("cristales energia mayor a 50 o igual")
mayor_igual_50=filtrar_cristales_superiores(cristales)
for s in mayor_igual_50:
    print("los cristales energia mayor a 50: " ,s)

print("solo nombres")
nombres=mapear_nombres(cristales)
for n in nombres:
    print("los nombres son: " ,n)

print(cristales[1])
print("Probando el metodo absorver")
prueba=cristales[1]
nueva_energia=prueba.absorber(3.5)
print(f"la nueva energia de {cristales[1]} es : nueva_energia")