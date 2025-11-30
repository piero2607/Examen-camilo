class Movie:
    def __init__(self,titulo,genero,puntuacion):
        if titulo is None or not isinstance(titulo,str) or titulo.strip()=="":
            raise ValueError("el titulo debe no puede ser numero ni estar vacio")
        generos_validos=["accion","comedia","drama","terror"]
        if not isinstance(genero,str) or genero.lower() not in generos_validos:
            raise ValueError(f"genero invalido debe ser uno de los generos validos {generos_validos}")
        if not isinstance(puntuacion,(int,float)) or not (0<=puntuacion<=10):
            raise ValueError("la puntuacion debe estar entre cero y 10 y ser entero o flotante")
        self.__titulo=titulo
        self.__genero=genero
        self.__puntuacion=float(puntuacion)

    def getTitulo(self):
        return self.__titulo
    def getGenero(self):
        return self.__genero
    def getpuntuacion(self):
        return self.__puntuacion

    def setTitulo(self,nuevotitulo):
        if nuevotitulo is None or not isinstance(nuevotitulo,str) or nuevotitulo.strip()=="":
            raise ValueError("el titulo no puede estar vacio o ser numerico")
        self.__titulo=nuevotitulo
    def setGenero(self,nuevogenero):
        generos_validos=["accion","comedia","drama","terror"]
        if not isinstance(nuevogenero,str) or nuevogenero.lower() not in generos_validos:
            raise ValueError(f"el genero no esta en la lista validos: {generos_validos}")
        self.__genero=nuevogenero
    def setPuntuacion(self,nuevapuntuacion):
        if not isinstance(nuevapuntuacion,(int,float)) or not (0<=nuevapuntuacion<=10):
            raise ValueError("la puntuacion debe ser un numero entre 0 y 10")
        self.__puntuacion=float(nuevapuntuacion)

    def __str__(self):
        return f"(MOVIE(titulo: {self.__titulo},Genero: {self.__genero}, puntuacion: {self.__puntuacion}"


peliculas_datos = [
    ("Matrix", "acción", 8.7),
    ("La La Land", "drama", 7.5),
    ("Scary Movie", "comedia", 6.2),
    ("El conjuro", "terror", 7.9),
    ("Película inválida", "accion", 5.0),
    ("lola", "comedia", 9.0),
    ("Peli loca", "acción", 10.0)
]
print(peliculas_datos)

for p in peliculas_datos:
    print(p[2])
mayor_7=filter(lambda p:p[2]<=7,peliculas_datos)
for p in mayor_7:
    print(p)