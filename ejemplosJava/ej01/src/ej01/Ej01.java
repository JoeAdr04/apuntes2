/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ej01;

public class Ej01 {


    public static void main(String[] args) {
        // TODO code application logic here
        VideoJuego v1 = new VideoJuego("Left 4", "pc", 4);
        VideoJuego v2 = new VideoJuego("Fortnite");
        System.out.println(v1);
        System.out.println(v2);
        v1.agregarJugadores();
        v1.agregarJugadores();
        v2.agregarJugadores(40);
        v2.agregarJugadores(40);
        System.out.println(v1);
        System.out.println(v2);
        
    }
    
}
