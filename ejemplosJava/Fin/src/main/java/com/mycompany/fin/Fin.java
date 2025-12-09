/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.fin;

/**
 *
 * @author erenb
 */
public class Fin {

    public static void main(String[] args) {
        System.out.println("Hello World!");
       Consultorio c= new Consultorio("medicos.json","consultas.json");
       c.altaMedico(new Medico(12, "jUAN", "VAZQUEZ", 4));
       c.altaConsulta(new Consulta(1234,"jose","choque",12, 25, "diciembre",2025));
       c.cambia("enero", 3);
    }
}
