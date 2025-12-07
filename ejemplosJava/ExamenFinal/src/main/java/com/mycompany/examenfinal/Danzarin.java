/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.examenfinal;


public class Danzarin extends Persona{
    private int nroParticiopaciones;

    public Danzarin(int nroParticiopaciones, String nombre, String genero, int edad) {
        super(nombre, genero, edad);
        this.nroParticiopaciones = nroParticiopaciones;
    }

    public Danzarin() {
        super();
    }

    public int getNroParticiopaciones() {
        return nroParticiopaciones;
    }

    public void setNroParticiopaciones(int nroParticiopaciones) {
        this.nroParticiopaciones = nroParticiopaciones;
    }

    @Override
    public String toString() {
        return super.toString()+ "Danzarin{" + "nroParticiopaciones=" + nroParticiopaciones + '}';
    }
    
    
    
}
