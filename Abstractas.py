from abc import ABC , abstractmethod
class Persona(ABC):
    def __init__(self, nombre, paterno, materno, edad):
        self._nombre = nombre
        self._paterno = paterno
        self._materno = materno
        self.edad = edad
        
    @abstractmethod
    def mayorDeEdad(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, reg):
        super().__init__(nombre, paterno, materno, edad)
        self.sueldo = sueldo
        self.regProfesional = reg
        
    def __str__(self):
        return f"Nombre: {self._nombre} Mayor de edad:{self.mayorDeEdad()}"
    
    def mayorDeEdad(self):
        return self.edad>18
    
    
class Empleado:
    def __init__(self,registro):
        self._registro = registro    
    
    def __str__(self):
        return f"Registro: {self._registro} "
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
        
    def __str__(self):
        return f"Nombre: {self._nombre} "
        
class Policia:
    def __init__(self, grado):
        self._grado = grado
        
    def __str__(self):
        return f"Grado: {self._grado} "
        
class JefePolicia(Empleado, Persona, Policia):
    
    def __init__(self, registro, nombre, grado):
        Empleado.__init__(self,registro)
        Persona.__init__(self,nombre)
        Policia.__init__(self,grado)
        
    def __str__(self):
        return Persona.__str__(self) + Empleado.__str__(self) + Policia.__str__(self)

class Main():
    
    #d = Docente ("Jhonny","Felipez", "Andrade",17, 233333, 1234)
    #print (d)
    jp = JefePolicia(1234, "lara", "capitan")
    print(jp)
