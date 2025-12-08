class LunarCrystal:
    def __init__(self,nombre,energia_lunar,categorias):
        if not isinstance(nombre,str) or nombre.strip()=="":
            raise ValueError("El nombre  no puede estar vacio y debe ser una cadena")
        if not isinstance(energia_lunar,(int,float)) or not (0.0<=energia_lunar<=100.0):
            raise ValueError("La energia lunar debe estar en el rango de 0-100")
        if not isinstance(categorias,list) or len(categorias)==0:
            raise ValueError("La categoria debe contener al menos un elemento")
        categorias_validas = ["arcano", "diurno", "nocturno", "luminoso",
                              "poderoso", "místico", "protector", "energético",
                              "sanador", "cosmico", "visionario"]
        for categoria in categorias:
            if not isinstance(categoria,str) or categoria.strip()=="":
                raise ValueError("LA categoria debe ser un string no vacio")
            if categoria not in categorias_validas:
                raise ValueError(f"La categoria debe ser al menos uno de estos: {categorias_validas}")
        if len(categorias)!=len(set(categorias)):
            raise ValueError("no pueden haber categorias repetidas")
        self.__categorias=categorias.copy()
        self.__nombre=nombre.strip()
        self.__energia_lunar=float(energia_lunar)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def energia_lunar(self):
        return self.__energia_lunar

    @energia_lunar.setter
    def energia_lunar(self,valor):
        if not isinstance(valor,(int,float)) or not (0.0<=valor<=100.0):
            raise ValueError("La energia lunar debe estar entre 0-100")
        self.__energia_lunar=valor

    @property
    def categorias(self):
        return self.__categorias.copy()

    def absorber(self,cantidad):
        if not isinstance(cantidad,(int,float)) or cantidad<=0:
            raise ValueError("La cantidad debe ser un numero positivo")
        nueva_energia=self.__energia_lunar+cantidad
        if nueva_energia>100.0:
            self.__energia_lunar=100.0
            print(f"{self.__nombre} alcanzo el maximo 100")
        else:
            self.__energia_lunar=nueva_energia
        return self.__energia_lunar

    def __str__(self):
        return f"Nombre: {self.__nombre}--Energia: {self.energia_lunar}--Categorias:{self.__categorias}"

