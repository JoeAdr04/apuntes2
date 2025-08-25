class Banco:
    def __init__(self, nombre:str, capital:float):
        self.__nombre = nombre
        self.__capital = capital
        self.__cliente = []
        self.__saldo = []
        
    def __str__(self):
        cad = ""
        for i in range(len(self.__cliente)):
            cad = cad +f"cliente :{self.__cliente[i]}, saldo :{self.__saldo[i]}\n"
            
        return f"nombre:{self.__nombre}, capital:{self.__capital}\n{cad}"
    
    def agregarCliente(self, cliente, saldo):
        self.__cliente.append(cliente)
        self.__saldo.append(saldo)
        
    
class Main():
    
    banco = Banco("Fassil", 0)
    banco.agregarCliente("Manuel", 2000)
    banco.agregarCliente("Ronald", 2500)
    banco.agregarCliente("Adrian", 50)
    banco.agregarCliente("Mariluz", 2000)
    
    print(banco)