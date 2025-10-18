/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package her;

/**
 *
 * @author Jaeger
 */
public class Her {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        //Animal a1 = new Animal("Leon", 4, "masculino");
        Mascota m1 = new Mascota("perro", 2, "masculino", "joel");
        System.out.println(m1);
        m1.mostrar();
    }
    
}
