/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package filaa;

/**
 *
 * @author Jaeger
 */
public class Panaderia extends Negocio {
    private String[] trabajadores = {"juan", "jose", "luis"};
    private String[] productos = {"Galletas", "Biscochos", "Panes"};
    private String[] equipos = {"Horno", "amasadora", "Batidora"};

    public Panaderia(double capital, String nombre, String propietario) {
        super(capital, nombre, propietario);
    }

    public Panaderia() {
        super();
    }
}