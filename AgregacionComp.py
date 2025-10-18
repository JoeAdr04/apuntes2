class Persona:
    def __init__(self, nom, apel, edad):
        self.__nombre=nom 
        self.__apellido=apel
        self.__edad=edad
    
    def __str__(self):
        return f"La persona: {self.__nombre} {self.__apellido}, de edad {self.__edad}"
    
    def getNombre(self):
        return self.__nombre
    
class Vehiculo:
    def __init__(self, placa, chasis, dueño):
        self.placa = placa
        self.chasis = chasis
        self.dueño = dueño
        self.pasajeros = []
        
    def verifica(self, p):
        for i in range(len(self.pasajeros)):
            if (self.pasajeros[i] == p):
                return True
        
    def agregaPasajeros(self, p:Persona):
        if(len(self.pasajeros) == 0):
            self.pasajeros.append(p)
        if(self.verifica(p)):
            print("el pasajero ya existe")
        else:
            self.pasajeros.append(p)
        
    def __str__(self):
        cad = f"placa:{self.placa}, chasis:{self.chasis}\n"
        for i in range (len(self.pasajeros)):
            cad = cad + f"pasajero 1:{self.pasajeros[i]}\n"
        return cad

class Main():
    p1 = Persona("fernando", "choque", 25)
    p2 = Persona("alejandro", "perez", 23)
    p3 = Persona("clara", "chia", 22)
    
    v = Vehiculo("1234asd", "xdxdxd",p3)
    v.agregaPasajeros(p1)
    v.agregaPasajeros(p2)
    v.agregaPasajeros(p3)
    v.agregaPasajeros(p3)
    v.agregaPasajeros(p3)
    v.agregaPasajeros(p3)
    v.agregaPasajeros(p3)
    v.agregaPasajeros(p3)
    print(v)
    #crear una funcion que agregue solo psasajeros que no estaban en el auto
    