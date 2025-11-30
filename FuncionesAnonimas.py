from functools import reduce

peliculas = [
    {"nombre": "El padrino", "valoracion": 9.2, "duracion": 175},
    {"nombre": "Toy Story", "valoracion": 8.9, "duracion": 154},
    {"nombre": "El señor de los anillos", "valoracion": 8.3, "duracion": 81},
    {"nombre": "Forrest Gump", "valoracion": 8.8, "duracion": 142},
]
ordenar_valkoracio=sorted(peliculas,key=lambda p:p["valoracion"],reverse=True)
print(ordenar_valkoracio)

ordenar_nombre=sorted(peliculas,key=lambda p:p["nombre"])
print(ordenar_nombre)

mayor_120=list(filter(lambda p:p["duracion"]>120,peliculas))
print(mayor_120)

solo_nombre=list(map(lambda p:p["nombre"],peliculas))
print(solo_nombre)

ventas = [1500, 800, 2200, 600, 3500, 950, 1200, 450]

total_ventas=reduce(lambda s,v:s+v,ventas,0)
print(total_ventas)

ventas_mayor_1000=list(filter(lambda v:v>1000,ventas))
print(ventas_mayor_1000)

frases = [
    "Python es genial",
    "Me gusta programar",
    "Hola mundo",
    "La programación funcional es interesante",
    "Hola"
]

mayusculas=list(map(lambda m:m.upper(),frases))
print(mayusculas)

frase_mayor_3=list(filter(lambda f:len(f.split())>3,frases))
print(frase_mayor_3)

total_palabras=reduce(lambda acc,f:acc+len(f.split()),frases,0)
print(total_palabras)


