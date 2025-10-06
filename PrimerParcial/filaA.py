from multimethod import multimethod
#implementacion de la pregunta 2:
class Parqueo:
    def __init__(self, nv, tariho, vehiculo, tiempo):
        self.__nroVehiculos = nv
        self.__tarifaHora = tariho
        self.__vehiculos = vehiculo
        self.__tiempo = tiempo
        
    def __str__(self):
        cad = f"Nrovehiculos: {self.__nroVehiculos}, tarifaPorHora: {self.__tarifaHora}\n"
        for i in range (len(self.__vehiculos)):
            cad = cad+f"[{self.__vehiculos[i][0]}][{self.__vehiculos[i][1]}], [{self.__tiempo[i][0]}][{self.__tiempo[i][1]}]\n"
        return cad
    #Sobrecarga un operador para implementar la salida de un vehiculo con placa P  mostrando ademas el importe que deben cancelar
    def __add__(self, p):
        for i in range(len(self.__vehiculos)):
            if (self.__vehiculos[i][0] == p):
                importe = (self.__tiempo[i][1]-self.__tiempo[i][0])*self.__tarifaHora
                print(f"Importe a cancelar: {importe}")
                self.__vehiculos.pop(i)
                self.__tiempo.pop(i)
                break
            
            
    def __sub__(self, p):
        placa, cond, t1, t2 = p
        v = [placa, cond]
        t  =[t1,t2]
        self.__vehiculos.append(v)
        self.__tiempo.append(t)
        
        
    #Sobrecargar un metodo para:
    # - calcular el ingreso total de todos los vehiculos:
    @multimethod
    def ingreso(self):
        importe = 0
        for i in range(len(self.__vehiculos)):
            horas = (self.__tiempo[i][1]-self.__tiempo[i][0])
            importe = importe + horas*self.__tarifaHora
        return importe
    # - calcular el ingreso total que pagaron los vehiculos que estuvieron parqueados k horas:
    @multimethod
    def ingreso(self, k:int):
        importe = 0
        for i in range(len(self.__vehiculos)):
            horas = self.__tiempo[i][1]-self.__tiempo[i][0]
            if(horas == k):
                importe = importe + horas*self.__tarifaHora
        return importe
    
#implementacion de la pregunta 3:
class Negocio:
    def __init__(self, capital=0, nombre="", propietario=""):
        self._capital = capital
        self._nombre = nombre
        self._propietario = propietario
        
    def getCapital(self):
        return self._capital
    
    def __str__(self):
        return f"Negocio: [Capital: {self._capital}, Nombre: {self._nombre}, Propietario: {self._propietario}]"
    
    # Definir un metodo que compare dos atributos de todos los objetos definidos
    def compara(self, otro):
        if(isinstance(otro, Negocio)):
            if(self._capital == otro._capital  and self._propietario == otro._propietario):
                print("El propietario y capital son iguales")
            elif(self._capital == otro._capital  or self._propietario == otro._propietario):
                print("Solo el propietario o el capital son iguales")
            else:
                print("Los atributos no son iguales")
    
class Peluqueria(Negocio):
    def __init__(self, capital=0, nombre="", propietario=""):
        super().__init__(capital, nombre, propietario)
        self.__peluqueros=["jose", "max"]
        self.__clientes = []
        self.__productos =["shampoo", "tinte", "secadora"]
        
class Salteñeria(Negocio):
    def __init__(self, capital=0, nombre="", propietario="", ub=""):
        super().__init__(capital, nombre, propietario)
        self.__ubicacion = ub
        self.__repartidores = []
        self.__reservas = []
        
class Panaderia(Negocio):
    def __init__(self, capital=0, nombre="", propietario=""):
        super().__init__(capital, nombre, propietario)
        self.__trabajadores = ["juan", "jose", "luis"]
        self.__productos = ["Galletas", "Biscochos", "Panes"]
        self.__equipos = ["Horno", "amasadora", "Batidora"]
        
#clase principal
class Main():
    #Pregunta 2
    vehiculos = [["1245axd", "Luis Jairo"],
                ["3456pib","Marcia Lira"],
                ["2576jux","Pablo Rubio"],
                ["3221lip","Rosa Jux"],
                ["3456kik","Saul Lopez"]]
    tiempo = [[2,5],[9,12],[10,12],[10,13],[10,11]]
    
    p = Parqueo(5,3,vehiculos, tiempo)
    #Sobrecarca un operador
    p+"2576jux"
    print(p)
    p-("1234asd", "joel", 4,9)
    print(p)
    #Sobrecarga un metodo
    print(p.ingreso())
    print(p.ingreso(3))
    
    #pregunta 3
    #b)Crea objetos de difrente forma
    p1 = Peluqueria(5000, "Smart Cut", "Vin Disel")
    p2 = Peluqueria()
    s = Salteñeria(4000, "Castor", "David Castro", "Av Buenos aires")
    pa1 = Panaderia()
    pa2 = Panaderia(2000, "don pepe", "Jose Martines")
    todos = [p1,p2,s,pa1,pa2]
    # c)Metodo que compare atributos
    for i in range(len(todos)):
        for j in range(i+1, len(todos)):
            todos[i].compara(todos[j])
    #Mostra negocio con mas capital
    may = 0
    for i in range(len(todos)):
        if(todos[i].getCapital()>may):
            may = todos[i].getCapital()
    for i in range(len(todos)):
        if(todos[i].getCapital() == may):
            print(f"Negocio con mas capital:\n{todos[i]}")
        