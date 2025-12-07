
package com.mycompany.examenfinal;

import java.util.ArrayList;

public class Fraternidad {
    private String nombre;
    private String danza;
    private ArrayList<Danzarin> d = new ArrayList();

    public Fraternidad(String nombre, String danza) {
        this.nombre = nombre;
        this.danza = danza;
    }

    public Fraternidad() {
    }
    
    public void agregarDanzarin(Danzarin d){
        this.d.add(d);
    }

    public String getNombre() {
        return nombre;
    }

    public String getDanza() {
        return danza;
    }

    public ArrayList<Danzarin> getD() {
        return d;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setDanza(String danza) {
        this.danza = danza;
    }

    public void setD(ArrayList<Danzarin> d) {
        this.d = d;
    }

    @Override
    public String toString() {
        return "Fraternidad{" + "nombre=" + nombre + ", danza=" + danza + ", d=" + d + '}';
    }
    
}
