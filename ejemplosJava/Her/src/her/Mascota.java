/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package her;

/**
 *
 * @author Jaeger
 */
public class Mascota extends Animal{ //ehereda de la clase padre animal
    private String dueño;
    
    public Mascota(String tip, int ed, String gen, String du){
        super(tip, ed, gen); //construcntor de la clase padre
        this.dueño = du; 
    }

    @Override
    public String toString() {
        return super.toString()+ "Mascota{" + "due\u00f1o=" + dueño + '}';
    }
    
    public void mostrar(){
        super.mostrar();
        System.out.println("datos de la clase hija");
    }
    
}
