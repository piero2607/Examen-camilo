class User:
    def __init__(self,username,email,age):
        if not isinstance(username,str) or username is None or username.strip()=="":
            raise ValueError("El nonmbre de usuario no puede ser numero o estar vacio")
        if not isinstance(email,str) or "@" not in email or "." not in email:
            raise ValueError("el email debe contener @ y .")
        if not isinstance(age,int) or not (14<=age<=120):
            raise ValueError("Edad invalida")
        self.__username=username
        self.__email=email
        self.__age=age
        self.__active=True

    def getUsername(self):
        return self.__username
    def getEmail(self):
        return self.__email
    def getAge(self):
        return self.__age
    def isActive(self):
        return self.__active

    def setEmail(self,new_email):
        if not isinstance(new_email,str) or "@" not in new_email or "." not in new_email:
            raise ValueError("El email debe contener @ y .")
        self.__email=new_email

    def setAge(self,new_age):
        if not isinstance(new_age,int) or not (14<=new_age<=120):
            raise ValueError("la edad debe estrar entre 14 y 120")
        self.__age=new_age

    def deactivate(self):
        self.__active=False
    def activate(self):
        self.__active=True

    def __str__(self):
        if self.__active==True:
            estado="Activo"
        else:
            estado="Inactivo"
        return f"(USERS :Nombre: {self.__username},Edad: {self.__age},Estado: {estado}"
