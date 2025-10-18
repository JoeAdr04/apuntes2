/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejer03;

/**
 *
 * @author Jaeger
 */
public class Planta {
    protected String color;
    
    public Planta(String p){
        this.color = p;
    }

    @Override
    public String toString() {
        return "Planta{" + "color=" + color + '}';
    }

    public String getColor() {
        return color;
    }
    
    
}
