package relaciones;


public class Cosas {
    private String nombre;
    private int codigo;
    
    public Cosas(String nom, int cod){
        this.nombre = nom;
        this.codigo = cod;
    }

    public String getNombre() {
        return nombre;
    }

    public int getCodigo() {
        return codigo;
    }

    @Override
    public String toString() {
        return "Cosas{" + "nombre=" + nombre + ", codigo=" + codigo + '}';
    }
    
}
