class Persona:
    def __init__(self, nombre, paterno, materno, ci, edad):
        self._nombre = nombre
        self._paterno = paterno
        self._materno = materno
        self._ci = ci
        self._edad = edad
        
class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, ci, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, ci, edad)
        self.__ru = ru   
        self.__matricula  = matricula
        
class Rector(Persona):
    def __init__(self, nombre, paterno, materno, ci, edad, anios, sueldo):
        super().__init__(nombre, paterno, materno, ci, edad)
        self.__anios = anios
        self.__sueldo = sueldo

class Carrera:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.estudiantes = []
        
    def agregaEstudiante(self, e:Estudiante):
        self.estudiantes.append(e)
    
class Facultad:
    def __init__(self, nombre, num):
        self.__nombre = nombre
        self.__nroCarreras = num
        self.__carreras = []
    
    def agregaCarrera(self, c:Carrera):
        self.__carreras.append(c)
    

class Universidad:
    def __init__(self, nombre, direccion,nombreRec, paterno, materno, ci, edad, anios, sueldo):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__rector = Rector( nombreRec, paterno, materno, ci, edad, anios, sueldo)
        self.__facultades = []
    
    def agregaFacultad(self, facu:Facultad):
        self.__facultades.append(facu)

class Main():
    
    u1 = Universidad("umsa", "la paz", "juab", "perez", "gutierrez", 1234, 40, 5, 24000)
    u1 = Universidad("umsa", "la paz", "juab", "perez", "gutierrez", 1234, 40, 5, 24000)
    u1 = Universidad("umsa", "la paz", "juab", "perez", "gutierrez", 1234, 40, 5, 24000)
    u1 = Universidad("umsa", "la paz", "juab", "perez", "gutierrez", 1234, 40, 5, 24000)