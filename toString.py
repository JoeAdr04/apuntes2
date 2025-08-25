class Alma:
    def __init__(self, cuerpo, sentido, albedrio):
        self.__cuerpo = cuerpo
        self.__sentido = sentido
        self.__albedrio = albedrio
        
    def mostrar(self):
        print(f"cuerpo : {self.__cuerpo}, sentido : {self.__sentido}, albedrio: {self.__albedrio}")
    
    #def __str__(self):
     #   return (f"cuerpo : {self.__cuerpo}, sentido : {self.__sentido}, albedrio: {self.__albedrio}")    
        
class Main():
    
    a = Alma("joel", 10, False)
    a.mostrar()
    print ("------diferencia __str__ ---------")
    print (a)