
package intefaces;


public abstract class Policia {
    protected double sueldo;
    protected String grado;

    public Policia(double sueldo, String grado) {
        this.sueldo = sueldo;
        this.grado = grado;
    }

    public Policia() {
        this.sueldo = 0.0;
        this.grado = "";
    }
    
    public abstract double getSueldo();

    public String getGrado() {
        return grado;
    }
    
    
}
