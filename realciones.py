class Vehiculo:
    def __init__(self, placa, conductor):
        self.__placa = placa
        self.__conductor = conductor        
    def __str__(self):
        return f"Placa:{self.__placa}, Conductor:{self.__conductor}"
class Parqueo:
    def __init__(self, nv, tarifa):
        self.__tarifa = tarifa
        self.__numVehiculos = nv
        self.__vehiculos = []
    def __str__(self):
        cad = f"Tarifa por hora: {self.__tarifa}, nroVehiculos = {self.__numVehiculos}\n"
        for i in range(self.__numVehiculos):
            cad = cad + f"{self.__vehiculos[i].__str__()}\n"
        return cad
    def agregarVehiculo(self, v):
        self.__vehiculos.append(v)
        self.__numVehiculos =self.__numVehiculos+1
        
class Tarifa:
    def __init__(self, valor, desc):
        self.__valor = valor
        self.__descuento = desc
        
    def __str__(self):
        return f"valor de tarifa:{self.__valor}, descuento: {self.__descuento}"
class Main():
    t = Tarifa(3,2.4)
    Parq = Parqueo(0,t )
    v1 = Vehiculo("1234asdf", "joel")
    v2 = Vehiculo("2345qwer", "Addrian")
    Parq.agregarVehiculo(v1)
    Parq.agregarVehiculo(v2)
    print(Parq)