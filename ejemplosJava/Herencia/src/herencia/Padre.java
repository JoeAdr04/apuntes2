/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia;

/**
 *
 * @author Jaeger
 */
public class Padre {
    protected String nombre;
    protected int edad;
    
    public Padre(){
        this.nombre = "";
        this.edad = 0;
    }
    public Padre(String nom, int ed){
        this.nombre = nom;
        this.edad = ed;
    }

    @Override
    public String toString() {
        return "Padre{" + "nombre=" + nombre + ", edad=" + edad + '}';
    }
    
}
