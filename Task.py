import random


class Task:
    def __init__(self,title,priority,completed=False):
        if not isinstance(title,str) or title.strip()=="":
            raise ValueError("El titulo no puede estar vacio")
        if not isinstance(priority,int) or not (1<=priority<=5):
            raise ValueError("la prioridad debe ser un numero entre 1 y 5")
        self.__title=title
        self.__priority=priority
        self.__completed=completed

    @property
    def title(self):
        return self.__title
    @property
    def priority(self):
        return self.__priority
    @property
    def completed(self):
        return self.__completed

    def mark_done(self):
        self.__completed=True

    def __str__(self):
        if self.__completed==True:
            estado="completada"
        else:
            estado="imcompleta"
        return f"{self.__title}-Prioridad: {self.__priority}-Estado: {estado}"

tareas_datos=[
    ("estudiar python", random.randint(1, 10) % 5 + 1),
    ("estudiar java", random.randint(1, 10) % 5 + 1),
    ("estudiar BBDD", random.randint(1, 10) % 5 + 1),
    ("",random.randint(1,10)%5+1), #error tarea
    ("estudiar django",random.randint(6,10))# error rango

]

tareas=[]

for tarea,prioridad in tareas_datos:
    try:
        t=Task(tarea,prioridad)
        tareas.append(t)
    except ValueError as e:
        print("ERRor al crear la tarea" ,e)
tareas[1].mark_done()
tareas[2].mark_done()

for i in range(2):
    try:
        titulo=input("ingresa que tarea quieres agregar:\n")
        prioridad_aleatoria=random.randint(1,10)%5+1
        tarea=Task(titulo,prioridad_aleatoria)
        tareas.append(tarea)
    except ValueError as e:
        print("Error al crear la tarea " ,e)

for j in tareas:
     print(j)

completadas=list(filter(lambda t: not t.completed,tareas))
for com in completadas:
    print("tareas incompletas: " ,com)

solo_titulos=list(map(lambda t:t.title,tareas))
print(solo_titulos)


