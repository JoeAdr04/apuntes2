/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package filaa;

/**
 *
 * @author Jaeger
 */
public 
class Salteñeria extends Negocio {
    private String ubicacion;
    private String[] repartidores = new String[50];
    private String[] reservas = new String[50];

    public Salteñeria(double capital, String nombre, String propietario, String ub) {
        super(capital, nombre, propietario);
        this.ubicacion = ub;
    }

    public Salteñeria() {
        super();
        this.ubicacion = "";
    }
}