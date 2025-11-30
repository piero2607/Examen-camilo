from functools import reduce

from User import *
class Activity:
    def __init__(self,user,type,duration):
        if not isinstance(user,User):
            raise ValueError("Usuario invalido")
        tipo_validos=["login","compra","comentario","visita"]
        if type not in tipo_validos:
            raise ValueError(f"Tipo invalido de ser uno de estos: {tipo_validos} ")
        if not isinstance(duration,(int,float)) or duration<=0:
            raise ValueError("Duracion invalida")
        self.__user=user
        self.__type=type
        self.__duration=duration

    def getUser(self):
        return self.__user
    def getDuration(self):
        return self.__duration

    def setDuration(self,new_duration):
        if not isinstance(new_duration,(int,float)) or new_duration<=0:
            raise ValueError("Duracion invalida")
        self.__duration=new_duration

    def __str__(self):
        return f"(Actividad: {self.__type}, Usuario: {self.__user.getUsername()}, Duracion: {self.__duration} min"


usuarios_datos = [
    ("Ana", "ana@mail.com", 22),
    ("  ", "bad@mail.com", 30),  # inválido username
    ("Luis", "luismail.com", 25),  # email inválido
    ("Mario", "mario@mail.com", 10),  # edad inválida
    ("Lucia", "lucia@mail.com", 40)
]
users=[]
for username,email,age in usuarios_datos:
    try:
        usuario=User(username,email,age)
        users.append(usuario)
        print("ok", usuario)
    except ValueError as e:
        print("Error creando usuario " ,e)

for nombre in users:
    print(nombre)

activities_data = [
    (users[0], "login", 5),
    (users[0], "compra", 10),
    ("no user", "login", 5),        # usuario inválido
    (users[1], "volar", 5),         # tipo inválido
    (users[1], "visita", -3),       # duración inválida
    (users[1], "comentario", 8)
]

activites=[]

for user,type,duration in activities_data:
    try:
        act=Activity(user,type,duration)
        activites.append(act)
        print("ok: " ,act)
    except ValueError as e:
        print("Error al crear la actividad" ,e)

actividades_activas=list(filter(lambda a:a.getUser().isActive(),activites))
for a in actividades_activas:
    print(a)

duracion=list(map(lambda a:a.getDuration(),actividades_activas))
print(duracion)

total_minutos=reduce(lambda acc,d:acc+d,duracion,0)
print(total_minutos)