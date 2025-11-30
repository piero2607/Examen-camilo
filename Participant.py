class Participant:
    def __init__(self,nombre,email):
        if not isinstance(nombre,str) or nombre.strip()=="" or nombre is None:
            raise ValueError("el nombre no puede estar vacio o ser entero")
        if not isinstance(email,str) or "@" not in email:
            raise ValueError("el email debe contener @")
        self.__nombre=nombre
        self.__email=email
        self.__pagado=False

    def getNombre(self):
        return self.__nombre
    def getEmail(self):
        return  self.__email
    def haspay(self):
        return self.__pagado

    def setNombre(self,nuevonombre):
        if not isinstance(nuevonombre,str) or nuevonombre.strip()=="":
            raise ValueError("el nombre no puede estar vacio o ser numerico")
        self.__nombre=nuevonombre.strip()
    def setEmail(self,nuevoemail):
        if not isinstance(nuevoemail,str) or "@" not in nuevoemail:
            raise ValueError("el email debe contener @")
        self.__email=nuevoemail.strip()

    def pay(self):
        self.__pagado=True
    def cancel(self):
        self.__pagado=False

    def __str__(self):
        if self.__pagado==True:
            estado="pagado"
        else:
            estado="no pagado"
        return f"Participante(Nombre: {self.__nombre}, (email: {self.__email}, estado: {estado}"

try:
    p1 = Participant("Piero", "piero123@example.com")
    p1.pay()
    print(p1)
except ValueError as e:
    print("Error:", e)

try:
    p2 = Participant("Carlos", "correo_sin_arroba")
except ValueError as e:
    print("Error:", e)

try:
    p3 = Participant("", "test@mail.com")
except ValueError as e:
    print("Error:", e)

try:
    p4 = Participant("Lucía", "luci@example.com")
    p4.setEmail("lucia_nuevo@mail.com")
    print(p4)
except ValueError as e:
    print("Error:", e)

try:
    p5 = Participant("Juan", "juan@mail.com")
    p5.setEmail("email_mal")
except ValueError as e:
    print("Error:", e)
