/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package her;

/**
 *
 * @author Jaeger
 */
public class Animal {
    protected String tipo;
    protected int edad;
    protected String genero;
    
    public Animal(String tip, int ed, String gen){
        this.tipo = tip;
        this.edad = ed;
        this.genero = gen;
    }

    public Animal(){
        this.tipo = "asdfasdf";
        this.edad = 1234;
        this.genero = "asdfasdf";
    }
    @Override
    public String toString() {
        return "Animal{" + "tipo=" + tipo + ", edad=" + edad + ", genero=" + genero + '}';
    }
    
    public void mostrar(){
        System.out.println("Datos de la lcase padre");
    }
    
    
}
