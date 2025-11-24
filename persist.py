import json
import os


class Arma:
    def __init__(self, cal, tipo, car):
        self.__calibre = cal
        self.__tipo = tipo
        self.__cargador = car
        
    def getCalibre(self):
        return self.__calibre
    def getTipo(self):
        return self.__tipo
    def getCargador(self):
        return self.__cargador
    def setCalibre(self, cal):
        self.__calibre = cal
    def setTipo(self, tipo):
        self.__tipo = tipo
    def setCargador(self, car):
        self.__cargador = car
        
    def toDict(self):
        return {
            "calibre":self.__calibre,
            "tipo": self.__tipo,
            "cargador" :self.__cargador
        }
    @staticmethod
    def dicAObj(dic):
        a = Arma(dic.get("calibre"), dic.get("tipo"),dic.get("cargador"))
        return a

class ArchivoArmas:
    def __init__(self, nombre:str):
        self.__nombre = nombre
        if(not os.path.exists(self.__nombre)):
            print("archivo creado")
            with open(self.__nombre, "w") as arch:
                json.dump([], arch, ensure_ascii=False, indent=2)

    def leer(self):
        with open(self.__nombre, "r") as arch:
            try:
                datos = json.load(arch)
            except Exception as e:
                print("ha fallado todo lo que podia fallar al leer", e)
                datos = []
        return datos
    
    def modificar(self, di):
        try:    
            with open(self.__nombre, "w") as arch:
                json.dump(di, arch,ensure_ascii=False, indent=2)
        except Exception as j:
            print("ha fallado todo lo que podia fallar al modificar", j)
            
    def agregarArma(self, ar:Arma):
        datos = self.leer()
        datos.append(ar.toDict())
        self.modificar(datos)
        
    def eliminarPorTipo(self, tipo):
        datos = self.leer()
        new = []
        for d in datos:
            if(d.get("tipo") != tipo):
                new.append(d)
        try:
            self.modificar(new)
        except Exception as e:
            print(e)
            
    def eliminarPorCalibre(self, calibre):
        datos = self.leer()
        new = []
        for d in datos:
            if(d.get("calibre") != calibre):
                new.append(d)
        try:
            self.modificar(new)
        except Exception as e:
            print(e)
            
    def editarTipoArma(self, tipo):
        datos = self.leer()
        new = []
        for d in datos:
            if(d.get("tipo") != tipo):
                new.append(d)
            else:
                aux = Arma.dicAObj(d)
                x = input("nuevo tipo de arma: ")
                aux.setTipo(x)
                new.append(aux.toDict())
        try:
            self.modificar(new)
        except Exception as e:
            print(e)
class Main():
    print ("asdf")
    opt = 100
    archivo = None
    archivo = ArchivoArmas("armas.json")
    while opt != 0:
        print('''
    Gestion de armas:
    2. adicionar un arma
    3. listar todas las armas
    4. eliminar un arma por el tipo
    5. eliminar un arma por el calibre
    6. editar por tipo
    0. salir
              ''')
        opt = int(input("Sleccione una opcion: "))
        if(opt == 2):
            if archivo is None:
                print("Primero cree el archivo (opción 1).")
            else:
                cal = int(input("ingrese calibre: "))
                tip = input("ingrese tipo de arma: ")
                car = int(input("ingrese nro de balas: "))
                archivo.agregarArma(Arma(cal,tip, car))
        elif(opt == 3):
            if archivo is None:
                print("Primero cree el archivo (opción 1).")
            else:
                print(archivo.leer())
        elif(opt == 4):
            if archivo is None:
                print("Primero cree el archivo (opción 1).")
            else:
                t = input("tipod e arma que desea eliminar: ")
                archivo.eliminarPorTipo(t)
        elif(opt == 5):
            if archivo is None:
                print("Primero cree el archivo (opción 1).")
            else:
                t = input("calibre del arma que desea eliminar: ")
                archivo.eliminarPorCalibre(t)
        elif(opt == 6):
            if archivo is None:
                print("Primero cree el archivo (opción 1).")
            else:
                t = input("tipo de arma que desea editar: ")
                archivo.editarTipoArma(t)

            
    
    
    
    #arr = archivo.leer()
    #for a in arr:
    #    b = Arma.dicAObj(a)
    #    print(b.getTipo())
    
    