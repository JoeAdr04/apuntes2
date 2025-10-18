/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package tostring;

/**
 *
 * @author Jaeger
 */
public class Alma {
    private String cuerpo;
    private int sentido;
    private boolean albedrio;
    
    public Alma(){
        this.cuerpo = "";
        this.albedrio = true;
        this.sentido = 0;
    }
    public Alma(String c,int s,boolean a){
        this.cuerpo = c;
        this.albedrio = a;
        this.sentido = s;
    }

    @Override
    public String toString() {
        return "Alma{" + "cuerpo=" + cuerpo + ", sentido=" + sentido + ", albedrio=" + albedrio + '}';
    }
    
}
