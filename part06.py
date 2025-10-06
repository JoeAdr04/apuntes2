from datetime import date
class ObjetoGeometrico:
    def __init__(self, color:str = "blanco", rellenado:bool=False):
        self._color = color
        self._rellenado = rellenado
        self._fechaDeCreacion = date.today()
        
    def __str__(self):
        return f"Objeto Geometrico:(color:{self._color}, rellenado:{self._rellenado}, fecha Creacion:{self._fechaDeCreacion})"
    
    def getGetColor(self):
        return self._color
    
    def getRellenado(self):
        return self._rellenado
    
    def getFechaCreacion(self):
        return self._fechaDeCreacion
    
    def setColor(self, col):
        self._color = col
        
    def setRellenado(self, rell):
        self._rellenado = rell
        
class Triangulo(ObjetoGeometrico):
    def __init__(self, color = "blanco", rellenado = False, lado1=1.0, lado2=1.0, lado3=1.0):
        super().__init__(color, rellenado)
        self.__lado1= lado1
        self.__lado2= lado2
        self.__lado3= lado3
    
    def __str__(self):
        return f"Triangulo: Lado1={self.__lado1} Lado2={self.__lado2} Lado3={self.__lado3}"
    
    def getLado1(self):
        return self.__lado1
    def getLado2(self):
        return self.__lado2
    def getLado3(self):
        return self.__lado3
    
    def getPerimetro(self):
        p = self.__lado1+ self.__lado2+self.__lado3
        return p
    
    def getArea(self):
        s = self.getPerimetro()/2
        a = (s*(s-self.__lado1)*(s-self.__lado2)*(s-self.__lado3))**(1/2)
        return a
    
    def mostrar(self):
        return super().__str__() +"\n"+ self.__str__()
    
class Main():
    a,b,c = input("ingrese los lados del trianuglo: ").split()
    col = input("cual es el color: ")
    rell = bool(input("tiene relleno(True/False): "))
    t = Triangulo(col, rell, float(a),float(b),float(c))
    print (t.mostrar())
    print ("Area del triangulo: "+str(t.getArea()))
    print ("Perimetro del triangulo: "+str(t.getPerimetro()))