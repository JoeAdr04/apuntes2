#x = int(input("ingres un numero: "))
#y = int(input("ingres otro: "))
'''arr = [1,2,3,4,5,6,7,8,9]
try:
    #print(f"division: {x/y}")
    for i in range(len(arr)+1):
        print(arr[i])
except IndexError as e:
    print(e)
'''
'''
while True:
    try:
        x = int(input("Ingres un numero"))
        print(x)
    except ValueError:
        print("ingresaste una letra we")
    
'''
#crear excepciones

class MayorDeEdadException(Exception):
    def __init__(self, m="no tiene mayoria de edad"):
        super().__init__(m)

class DatosVaciosException(BaseException):
    def __init__(self, m = "no se ingresaron datos"):
        super().__init__(m)
        
        
class ContactoInexistenteException(Exception):
    def __init__(self, mensaje = "no se encontro el contacto") -> None:
        super().__init__(mensaje)
        
class Agenda:
    def __init__(self):
        self.nombre=[]
        self.telefono=[]
        
    def agregarContacto(self, nom, tel):
        if(nom == "" or tel == 0):
            raise DatosVaciosException
        else:
            self.nombre.append(nom)
            self.telefono.append(tel)
            print("agregado con exito")
    
    def buscarContacto(self, c):
        sw = False
        pos = 0
        for i in range(len(self.nombre)):
            if(i == c):
                sw = True
                pos = i
                break
        if sw == True:
            return self.telefono[pos]
        else:
            raise ContactoInexistenteException
        
class Main():
    '''
    def verificaEdad(edad):
        if (edad<18):
            raise MayorDeEdadException("no es mayor")
        else:
            print("usted es mayor de edad")
    
    try:
        verificaEdad(17)
    except MayorDeEdadException as h:
        print("paso algo por que", h)
    '''    
    ag = Agenda()
    try:
        ag.agregarContacto("juan",0)
    except DatosVaciosException as l:
        print(l)