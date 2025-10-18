/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejer03;

/**
 *
 * @author Jaeger
 */
public class Arbol extends Planta{
    private int edad;

    public Arbol(String p, int e) {
        super(p);
        this.edad = e;
    }

    @Override
    public String toString() {
        return super.toString()+"Arbol{" + "edad=" + edad + '}';
    }
    
    
}
