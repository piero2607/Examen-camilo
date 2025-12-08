teams=[
    {
    "nombre": "Nave Horizon",
    "miembros": [
        {"name": "Aria", "role": "piloto", "experience": 5},
        {"name": "Darek", "role": "ingeniero", "experience": 3},
        {"name": "Silas", "role": "biólogo", "experience": 2}
    ]
    },
    {
    "nombre":"Nave Estelar",
    "miembros":[
        {"name": "Kael", "role": "piloto", "experience": 7},
        {"name": "Lena", "role": "ingeniero", "experience": 4},
        {"name": "Rex", "role": "táctico", "experience": 6}
        ]
    },
    {
    "nombre": "Nave Aurora",
    "miembros": [
        {"name": "Nova", "role": "piloto", "experience": 9},
        {"name": "Kai", "role": "ingeniero", "experience": 6},
        {"name": "Luna", "role": "científico", "experience": 7}
        ]
    }
]

for expe in teams:
    mayor_a_4=list(filter(lambda e:e["experience"]>4,expe["miembros"]))
    for l in mayor_a_4:
        print(f"los mienbros con experiencuia mayor a 4: ",l)

nombres=list(map(lambda n:n["nombre"],teams))
print("los nombres de las naves son: " ,nombres)

for nombre in teams:
    solo_nombres=list(map(lambda n:n["name"],nombre["miembros"]))
    for t in solo_nombres:
        print("Los nombres de todos son: " ,t)

for mayor in teams:
    experiencias=list(map(lambda e:e["experience"],mayor["miembros"]))
    maxima_experiencia=max(experiencias)
    print("El que tiene mayor experiencia es: " ,maxima_experiencia)

for nave in teams:
    mienbro_max_ex=max(nave["miembros"], key=lambda m:m["experience"])
    print(mienbro_max_ex)

lista_maximos=[]
for na in teams:
    for exp in na["miembros"]:
        lista_maximos.append(exp["experience"])
maxima_exp=max(lista_maximos)
print("la mayor experiencia global es: " ,maxima_exp)