package filaa;

public class Negocio {
    protected double capital;
    protected String nombre;
    protected String propietario;

    public Negocio(double capital, String nombre, String propietario) {
        this.capital = capital;
        this.nombre = nombre;
        this.propietario = propietario;
    }

    public Negocio() {
        this.capital = 0;
        this.nombre = "";
        this.propietario = "";
    }
    
    public double getCapital(){
        return capital;
    }

    @Override
    public String toString() {
        return "Negocio: [Capital: " + capital + ", Nombre: " + nombre + ", Propietario: " + propietario + "]";
    }

    public void compara(Negocio otro) {
        if (this.capital == otro.capital && this.propietario.equals(otro.propietario)) {
            System.out.println("El propietario y capital son iguales");
        } else if (this.capital == otro.capital || this.propietario.equals(otro.propietario)) {
            System.out.println("Solo el propietario o el capital son iguales");
        } else {
            System.out.println("Los atributos no son iguales");
        }
    }
}
