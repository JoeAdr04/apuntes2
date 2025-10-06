from multimethod import multimethod

class MiEntero:
    def __init__(self, valor):
        self.__valor = valor
        
    def getValor(self):#lo que obtiene un atributo
        return self.__valor
    
    #def __str__(self):
     #   return(f"valor :{self.__valor}")
    
    @multimethod
    def esPar(self): #normal
        if(self.__valor%2 ==0):
            return True
        else:
            return False
    
    @multimethod    
    @staticmethod
    def esPar(x:int): #metodo estatico que recibe un entero
        if(x%2 ==0):
            return True
        else:
            return False
    
    @multimethod    
    @staticmethod
    def esPar(obj:"MiEntero"):
        if(obj.getValor()%2 ==0 and isinstance(obj, MiEntero)):
            return True
        else:
            return False
    
class Server:
    def __init__(self, ip=192,database="db.sql",mac="12:a2:12"):
        self.__ip = ip
        self.__database = database
        self.__mac = mac
        
    def __str__(self):
        return(f"ip:{self.__ip}, database:{self.__database}, mac:{self.__mac}")
    
    def __mod__(self,otro): #operador para el modulo
        if(isinstance(otro, MiEntero)):
            return self.__ip + otro.getValor()
        
        elif(isinstance(otro, Server)):
            return self.__ip + otro.__ip

class Main():
    b = MiEntero(4)
    '''a = MiEntero(3)
    print(a.esPar())
    print(MiEntero.esPar(8))
    print(MiEntero.esPar(b))
    '''
    ## sobrecargar el operador * para dividir ip/valor (__mul__)
    server1 = Server(200)
    print(server1)
    server2 = Server(201,"data.sql")
    print(server2)
    print ("sobrebcarga el operador modulo %")
    x = server1%b
    print(x)
    print(server2%server1)
    
    

