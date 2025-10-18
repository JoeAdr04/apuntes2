from multimethod import multimethod
class Ram:
    def __init__(self, cap, marca, tipo):
        self.__capacidad = cap
        self.__marca = marca
        self.__tipo = tipo
        
    def getCapacidad(self):
        return self.__capacidad
    
    def setCapacidad(self,x):
        self.__capacidad = x
    
    def getMarca(self):
        return self.__marca
    def __str__(self):
        return f"capacidad: {self.__capacidad}, marca: {self.__marca}, tipo: tipo{self.__tipo}"
    
class DiscoDuro:
    def __init__(self,capa, marca, mod):
        self.__capacidad = capa
        self.__marca = marca 
        self.__modelo = mod
        
    def __str__(self):
        return f"capacidad:{self.__capacidad}, marca:{self.__marca}, modelo: {self.__modelo}"
    
    def getCapacidad(self):
        return self.__capacidad
    
    def setCapacidad(self,x):
        self.__capacidad = x
class Procesador:
    def __init__(self, mod, anio):
        self.modelo = mod
        self.anio = anio

class Computadora:
    def __init__(self, anio = 2025,mod ="i3", anio2=2024):
        self.__anioEnsamblae = anio
        self.__procesador=Procesador(mod, anio2)
        self.__ram = []
        self.__disco = []
        
    def agregarRam(self, ram):
        self.__ram.append(ram)
    def agregarDisco(self, disco):
        self.__disco.append(disco)
        
    def quitarRam(self, marca):
        for i in range(len(self.__ram)):
            if (self.__ram[i].getMarca() == marca):
                self.__ram.pop(i)
    # Sobrecargar el método modificarCapacidad(), uno modificando la ram y el otro 
    # modificando el disco duro. 
    @multimethod
    def modificarCapacidad(self, x:int):
        for i in range(len(self.__disco)):
            if(self.__disco[i].getCapacidad() < x):
                print("no puedes quitarle mas capacidad de la que tiene")
            else:
                self.__disco[i].setCapacidad(x)
    
    @multimethod
    def modificarCapacidad(self):
        for i in range(len(self.__ram)):
            if(self.__ram[i].getCapacidad() < 16):
                print("no puedes quitarle mas capacidad de la que tiene")
            else:
                self.__ram[i].setCapacidad(16)
    
    def __str__(self):
        cad = f"anioEnsambleaje:{self.__anioEnsamblae}\n"
        totalRam = 0
        for i in range (len(self.__ram)):
            totalRam = totalRam +self.__ram[i].getCapacidad()
        
        cad = cad + f"Total de ram:{totalRam}\n"
        totalDisco = 0
        for i in range (len(self.__disco)):
            totalDisco = totalDisco +self.__disco[i].getCapacidad()
        
        cad = cad + f"Total de disco:{totalDisco}\n"
        return cad
        
class Main():
    
    ram = Ram(128,"samsung", "ddr3")
    ram2 = Ram(128,"samsung", "ddr3")
    
    disco = DiscoDuro(256, "kingston", "nvme")
    
    comp = Computadora(2025, proc)
    comp.agregarDisco(disco)
    comp.agregarRam(ram)
    comp.agregarRam(ram2)
    
    ram.modificarCapacidad()
    print(comp)
    
    comp.modificarCapacidad(128)
    comp.modificarCapacidad()
    print(comp)