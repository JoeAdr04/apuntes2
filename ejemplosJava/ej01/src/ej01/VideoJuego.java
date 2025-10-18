/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ej01;

/**
 *
 * @author Jaeger
 */
public class VideoJuego {
    private String nombre;
    private String plataforma;
    private int cantJug;
    
    public VideoJuego(String nom){
        this.nombre ="";
        this.plataforma ="";
        this.cantJug =0;
    }
    
    public VideoJuego(String nom, String plat, int cant){
        this.nombre =nom;
        this.plataforma =plat;
        this.cantJug =cant;
    }

    @Override
    public String toString() {
        return "VideoJuego{" + "nombre=" + nombre + ", plataforma=" + plataforma + ", cantJug=" + cantJug + '}';
    }
    
    public void agregarJugadores(){
        this.cantJug = this.cantJug+1;
    }
    public void agregarJugadores(int n){
        this.cantJug = this.cantJug+n;        
    }
    
    
}
