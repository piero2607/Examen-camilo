from functools import reduce


class Suscription:
    def __init__(self,user='',plan=None,price=0.0,active=True):
        if not isinstance(user,str) or user.strip()=="":
            raise ValueError("el usuario no puede estar vacio ")
        planes_validos=["basic","pro","premium"]
        if plan not in planes_validos:
            raise ValueError(f"El plan debe ser uno de estos: {planes_validos}")
        if not isinstance(price,(int,float)) or price<=0:
            raise ValueError("el precio debe ser mayor que 0")
        self.__plan=plan
        self.__price=price
        self.__user=user
        self.__active=active

    @property
    def user(self):
        return self.__user
    @property
    def plan(self):
        return self.__plan
    @property
    def price(self):
        return self.__price
    @property
    def active(self):
        return self.__active

    @plan.setter
    def plan(self,nuevoplan):
        planes_validos = ["basic", "pro", "premium"]
        if nuevoplan not in planes_validos:
            raise ValueError(f"El plan debe ser uno de estos: {planes_validos}")
        self.__plan = nuevoplan

    @price.setter
    def price(self,nuevoprecio):
        if not isinstance(nuevoprecio, (int, float)) or nuevoprecio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self.__price = nuevoprecio

    @active.setter
    def active(self,valor):
        if self.__active is False and valor is True:
            raise ValueError("NO se puede activar una suscripcion ya cancelada")
        self.__active=valor

    def cancel(self):
        self.__active=False

    def __str__(self):
        if self.__active==True:
            estado="Activa"
        else:
            estado="Inactiva"
        return f"Usuario: {self.__user} | Plan: {self.__plan} | Precio: {self.__price}€ | Estado: {estado}"

suscripciones_datos = [
    ("piero", "premium", 15.99),
    ("ana", "pro",     11.50),
    ("mario", "basic", 7.99),
    ("luis", "gold",   20.00),       #  error plan
    ("", "basic",      5.00),       #  error user
    ("rosa", "premium", -10),       #  error precio
]

suscripciones=[]

for user,plan,price in suscripciones_datos:
    try:
        sus=Suscription(user,plan,price)
        suscripciones.append(sus)
    except ValueError as e:
        print("Erroa la crear suscripcion: " ,e)
suscripciones[1].cancel()
for s in suscripciones:
    print(s)

activas=list(filter(lambda a:a.active is True,suscripciones))
for s in activas:
    print("las asctivas son: " ,s)

total_mes=reduce(lambda acc,s:acc+s.price,activas,0)
print("total del mes es: " ,total_mes)