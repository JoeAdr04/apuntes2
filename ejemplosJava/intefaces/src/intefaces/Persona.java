
package intefaces;

public class Persona {
    protected String nombre;
    protected int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public Persona() {
        this.nombre = "";
        this.edad = 0;
    }
    
    public String getNombre(){
        return this.nombre;
    }
    public void mostrar(){
        System.out.print("hola");
    }
    public void mostrar(int x){
        System.out.print("hola"+ x);
    }
}

interface IPersona{
   public String getNombre();
}
