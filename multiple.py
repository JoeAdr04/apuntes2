class Coleccion:
    def __init__(self,a):
        self.__vec = [a]
        
    def __str__(self):
        cad = ""
        for i in range(len(self.__vec)):
            cad = cad + f"{self.__vec[i]}"
        return cad
    
    def mostrar(self):
        print(self.__vec)
class Main():
    a = (1,2,3,4,5,6,7,8,9)
    c = Coleccion(a)
    c.mostrar()