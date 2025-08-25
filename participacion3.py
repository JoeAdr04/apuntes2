import math

class PoligonoRegular():
    def __init__(self, n=3, lado=1, x=0, y=0):
        self.__n = n #numero de lados
        self.__lado = lado #longitud del lado
        self.__x = x
        self.__y = y
        
    def __str__(self):
        return f"n: {self.__n}, lado: {self.__lado}, x : {self.__x}, y :{self.__y}"
    
    def getPerimetro(self):
        p = self.__lado * self.__n
        return p
    
    def getArea(self):
        a = (self.__n*(self.__lado)**2)/(4*math.tan(math.pi/self.__n))
        return a
class Main():
    
    p =PoligonoRegular(4,3,2,2)
    p2 =PoligonoRegular(4)
        
    print (f"perimetro :{p.getPerimetro()}")
    print (f"Area :{p.getArea()}")
    