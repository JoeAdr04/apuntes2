class Automovil:
    def __init__(self, vel): ##cosntrictor, inicializador
        self.__velocidad = vel
        
    def __str__(self): #para impprimir (usar el print)
        return f"velocidad : {self.__velocidad}"
    
    def mostrar(self):
        print(f"velocidad : {self.__velocidad}") 

    
class Avion(): #crear la clase con 3 atributos
    def __init__(self, vel, dur, yer):
        self.__velocidad = vel 
        self.__dureza = dur #atributo privado
        self.__year = yer
    def __str__(self):
        return f"velocidad:{self.__velocidad} \n dureza:{self.__dureza} \n año:{self.__year}"
        #\n --> salto de linea
    
    def getDureza(self): ##getter (para obtener datos )
        return self.__dureza
    
    def setDureza(self, dur): ## setter (Modifica o actualiza)
        self.__dureza = dur
    
    def mostrar(self):
        print(f"velocidad:{self.__velocidad} dureza:{self.__dureza} año:{self.__year}")
        
        
        
class Main():
    a1 = Automovil(10)
    
    #print(a1)
    #print ("----------------")
    #a1.mostrar()
    
    avion = Avion(12,24,2025)
    print("avion")
    print(avion.getDureza())
    #print(avion.velocidad)
    print("modificando el valor de la dureza")
    avion.setDureza(50)
    print(avion.getDureza())
    
    