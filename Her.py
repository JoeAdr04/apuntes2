class Padre:
    def __init__(self, nombre=None, edad = None):
        self._nombre = nombre
        self.__edad = edad
    
    def __str__(self):
        return f"nombre:{self._nombre}, edad: {self.__edad}"
    
class Hija(Padre):
    def __init__(self, nombre=None, edad=None, pasaje = None):
        super().__init__(nombre, edad)
        self.__pasaje = pasaje
        
    def __str__(self):
        return super().__str__() + f"\npasaje:{self.__pasaje}"
    
    def cambiar(self, n):
        self._nombre = n
    
class Main():
    
    o1 = Hija("jovana", 25, 4.4)
    print(o1)
    o1.cambiar("juana")
    print(o1)