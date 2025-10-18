class Libro:
    def __init__(self, tit, ed, aut):
        self.__titulo = tit
        self.__edicion = ed
        self.__autor = aut
    
    def getAutor(self):
        return self.__autor
    
    def __str__(self):
        return f"titulo: {self.__titulo}, edicion: {self.__edicion}, autor: {self.__autor}"
        
class Estante:
    def __init__(self, tipo, tam,cant):
        self.__tipoMat = tipo
        self.__tamanio = tam
        self.__cantMax = cant
        self.__libros =[] #almacena objetos de la clase libro
        
    def agregarLibro(self, lib:Libro):
        self.__libros.append(lib)
        
    def eliminar(self, titulo):
        for i in range(len(self.__libros)):
            if (self.__libros[i] == titulo):
                self.__libros.pop(i)

    def mostrar(self, x:str):
        for lib in self.__libros:
            if(lib.getAutor() == x):
                print(lib)
                
   
    
class Main():
    l1 = Libro("la Mancha", 2018, "servantes")
    l2 = Libro("padre rico", 2020, "asdfasdf")
    
    e = Estante("metal", 12, 50)
    e.agregarLibro(l1)
    e.agregarLibro(l2)
    e.eliminar("la mancha")
    e.mostrar("asdfasdf")