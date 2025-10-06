package filaa;


public class Peluqueria extends Negocio {
    private String[] peluqueros = {"jose", "max"};
    private String[] clientes = new String[50];
    private String[] productos = {"shampoo", "tinte", "secadora"};

    public Peluqueria(double capital, String nombre, String propietario) {
        super(capital, nombre, propietario);
    }

    public Peluqueria() {
        super();
    }
}