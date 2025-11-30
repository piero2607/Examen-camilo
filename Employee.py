class Employee:
    def __init__(self,nombre,horas,precio):
        if not isinstance(nombre,str) or nombre.strip()=="":
            raise ValueError("el nombre no puede ser numerico o estar vacio")
        if not isinstance(horas,int) or not (1<=horas<=200):
            raise ValueError("las horas deben estar entre 1 y 200")
        if not isinstance(precio,(int,float)) or precio<=5:
            raise ValueError("el precio debe ser un numero mayor a 5")
        self.__nombre=nombre.strip()
        self.__horas=horas
        self.__precio=float(precio)

    def getNombre(self):
        return self.__nombre
    def getHoras(self):
        return self.__horas
    def getPrecio(self):
        return self.__precio

    def setHoras(self,nuevaHoras):
        if not isinstance(nuevaHoras,int) or not (1<=nuevaHoras<=200):
            raise ValueError("las horas deben estar entre 1 y 200 y ser numerico")
        self.__horas=nuevaHoras
    def calcular_salarios(self):
        return self.__horas*self.__precio

    def __str__(self):
        return f"Empleado(Nombre: {self.__nombre}, Salario Total: {self.calcular_salarios()}"

empleados_datos = [
    ("Piero", 160, 12),
    ("Laura", 120, 10),
    ("luca", 150, 20),          # Inválido
    ("Carlos", 180, 15),    # Inválido: horas > 200
    ("Ana", 100,6)         # Inválido: precio <= 5
]
empleados=[]
try:
    for nombre,horas,precio in empleados_datos:
        empleado=Employee(nombre,horas,precio)
        empleados.append(empleado)
        print(empleado)
except ValueError as e:
    print("Error al crear empleados" ,e)
salarios=list(map(lambda e:e.calcular_salarios(),empleados))
print(salarios)
info=list(map(lambda e:(e.getNombre(),e.calcular_salarios()),empleados))
print(info)