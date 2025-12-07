/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.examenfinal;

/**
 *
 * @author erenb
 */
public class ExamenFinal {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        ArchivoFraternidad arch = new ArchivoFraternidad();
        /*Fraternidad f = new Fraternidad("frate", "diablada");
        Fraternidad f2= new Fraternidad("frate2", "caporal");
        Danzarin d1 = new Danzarin(4, "jose", "masculino", 18);
        Danzarin d2 = new Danzarin(7, "maria", "femenino", 22);
        Danzarin d3 = new Danzarin(3, "luis", "masculino", 27);
        Danzarin d4 = new Danzarin(1, "segundino", "masculino", 17);
        f.agregarDanzarin(d1);
        f.agregarDanzarin(d2);
        f.agregarDanzarin(d3);
        f.agregarDanzarin(d4);
        
        
        arch.agregarFraternidad(f);
        */
        arch.promedioEdad("masculino");
        arch.mostrarParticipaciones("frate");
        //rch.eliminarPersona("luis");
        System.out.println(arch.leerTodo());
        
    }
}
