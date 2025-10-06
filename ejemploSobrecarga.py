class Sobrecarga():
    
    def __init__(self, a):
        self.__a = a
    
    def __mul__(self, b):
        return self.__a - b
    
    #python isinstance(a, int)
    #java instaceof(a, Sobrecarga)
    
class Celular:
    def __init__(self, nroTelf, dueño, espacio, ram, nroApp):
        self.__nroTel = nroTelf
        self.__dueño = dueño
        self.__espacio = espacio
        self.__ram = ram 
        self.__nroApp = nroApp
        
    def __mul__(self, a): #sobrecarga del operador *
        self.__nroApp = self.__nroApp+a
        
    def multiplicar(self, a=10): #sobrecarga del operador *
        self.__nroApp = self.__nroApp+a
        
    #sobrecargar el operado - para cambiar al dueño del celular:
    
    def __sub__(self, a):
        self.__dueño = a
    
    def __str__(self):
        return (f"Celular:{self.__nroTel}, Aplicaciones: {self.__nroApp}, dueño: {self.__dueño}")
class Auto:
    def __init__(self, placa=0, gasolina=10, color="blanco"):
        self.__placa = placa
        self.__gasolina = gasolina
        self.__color = color
        
    def __sub__(self, otro):
        if(isinstance(otro, Auto)):
            return self.__gasolina + otro.__gasolina
        else:
            print("no se trata de un auto")
            
class Planta:
    def __init__(self, color):
        self.__color = color
        
    def __str__(self):
        return f"color:{self.__color}"
class MateriaPrima:
    
    def __init__(self, costo):
        self.__costo = costo
        
    def __str__(self):
        return f"costo: {self.__costo}"
        
class Arbol(Planta, MateriaPrima):
    def __init__(self, color, costo, edad):
        Planta.__init__(self, color)
        MateriaPrima.__init__(self, costo)
        self.__edad = edad
        
    def __str__(self):
        return Planta.__str__(self) + MateriaPrima.__str__(self) + f"edad: {self.__edad}"
        
class Main():
    
    a = Arbol("negro", 44, 450)
    print(a)
    #a = Auto(1234, 15,"rojo")
    #b = Auto()
    
    #sumaGasolina = a-b
    #print(sumaGasolina)
    
    celu = Celular(69953348, "adrian", 246, 57, 4)
    print(f"antes{celu}")
    
    celu*0
    celu-"Alejandro"
    
    print(f"despues{celu}")
    
    