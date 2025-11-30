from functools import reduce


class Foot:
    def __init__(self,nombre,calorias,cantidad):
        if not isinstance(nombre,str) or nombre.strip()=="":
            raise ValueError("el nombre debe ser texto no vacio")
        if not isinstance(calorias,(int,float)) or calorias<=0:
            raise ValueError("Las calorias deben ser un numero positivo")
        if not isinstance(cantidad,int) or not (10<=cantidad<=500):
            raise ValueError("la cantidad debe ser un numero entre 10 y 500 gramos")
        self.__nombre=nombre
        self.__calorias=float(calorias)
        self.__cantidad=cantidad

    def getNombre(self):
        return self.__nombre
    def getCalorias(self):
        return self.__calorias
    def getCantidad(self):
        return self.__cantidad

    def setCalorias(self,nuevacalorias):
        if not isinstance(nuevacalorias,(int,float)) or nuevacalorias<=0:
            raise ValueError("las calorias deben ser un numero positivo")
        self.__calorias=nuevacalorias
    def setCantidad(self,nuevacantidad):
        if not isinstance(nuevacantidad,int) or not (10<=nuevacantidad<=500):
            raise ValueError("La cantidad debe estar entre 10 y 500")
        self.__cantidad=nuevacantidad

    def totalcalorias(self):
        return self.__calorias*self.__cantidad/100

    def __str__(self):
        return f"Food({self.__nombre}, {self.__calorias} cal/100g, {self.__cantidad}g)"

alimentos_datos = [
    ("Manzana", 52, 150),
    ("Pan", 265, 50),
    ("Pollo", 239, 200),
    ("Chocolate", 540, 20),
    ("", 80, 100),         # Inválido
    ("Queso", -20, 50),    # Inválido
    ("Arroz", 130, 600)    # Inválido
]
alimentos=[]
for nombre,calorias,cantidad in alimentos_datos:
    try:
        comida1=Foot(nombre, calorias, cantidad)
        alimentos.append(comida1)
        print(comida1)
    except ValueError as e:
        print("Error al crear alimento" ,e)
total=reduce(lambda acc,food:acc+food.totalcalorias(),alimentos,0)
print(total)