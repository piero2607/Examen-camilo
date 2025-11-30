class Pet:
    def __init__(self,nombre,especie,edad):
        if nombre is None or not isinstance(nombre,str) or nombre.strip()=="":
            raise ValueError("el nombre no puede estar vacio o ser un entero")
        self.__nombre=nombre.strip()
        if especie is None or not isinstance(especie,str) or especie.strip()=="":
            raise ValueError("la especie no puede ser numero o estar vacio")
        self.__especie=especie.strip()
        if not isinstance(edad,int) or edad<=0:
            raise ValueError("la edad debe ser mayor que cero y un entero")
        self.__edad=edad
        self.__vacunada=False
        self.__vacunar()

    def getNombre(self):
        return self.__nombre
    def getEspecie(self):
        return self.__especie
    def getEdad(self):
        return self.__edad

    def setNombre(self,nuevo_nombre):
        if not isinstance(nuevo_nombre,str) or nuevo_nombre.strip()=="":
            raise ValueError("el nombre debe ser un texto no vacio")
        self.__nombre=nuevo_nombre.strip()
    def setEdad(self,nuevaedad):
        if not isinstance(nuevaedad,int) or nuevaedad<=0:
            raise ValueError("la edad debe ser mayor que cero y un numero entero")
        self.__edad=nuevaedad

    def __vacunar(self):
        self.__vacunada=True

    def __str__(self):
        if self.__vacunada==True:
            estado='vacunada'
        else:
            estado='no vacunada'
        return f"Pet(Nombre: {self.__nombre},especie: {self.__especie},edad: {self.__edad} /{estado}"

try:
    mascota1=Pet("laica","gato",3)
    print(mascota1)
    mascota1.setNombre("laica")
    mascota1.setEdad(4)
    print(mascota1)
except ValueError as e:

    print("ERROR" ,e)
try:
    mascota_error = Pet("", "Perro", 2)
except ValueError as e:
    print(f"Error nombre vacío: {e}")

try:
    mascota_error = Pet("Rex", "Perro", -1)
except ValueError as e:
    print(f"Error edad negativa: {e}")

try:
    mascota_error = Pet("Rex", "", 2)
except ValueError as e:
    print(f"Error especie vacía: {e}")
