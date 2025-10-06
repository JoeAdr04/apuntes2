class Animal():
    def __init__(self, tipo="", edad=0, genero=""):
        self._tipo = tipo #protegido solo usa una barrita baja _
        self._edad = edad
        self._genero = genero
        
    def __str__(self):
        return f"tipo:{self._tipo}, edad:{self._edad}, genero:{self._genero}"
    
    
class Mascota(Animal):
    
    def __init__(self, tipo="", edad=0, genero="", dueno=""):
        super().__init__(tipo, edad, genero)
        self.__dueno = dueno
    
    def __str__(self):
        return super().__str__() + f" dueño :{self.__dueno}"
    
class Salvaje(Animal):
    
    def __init__(self, tipo="", edad=0, genero="", habitad=""):
        super().__init__(tipo, edad, genero)
        self.__habitad = habitad
        
    def __str__(self):
        return super().__str__() + f"habitad {self.__habitad}"
    
class Main():
    
    m1 = Mascota("gato", 8, "femenino", "Manuel")
    print(m1)
    m2 = Mascota()
    print(m2)