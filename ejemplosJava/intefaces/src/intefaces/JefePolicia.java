
package intefaces;


public class JefePolicia extends Policia implements IPersona{
    private int placa;
    Persona p;

    public JefePolicia(double sueldo, String grado, int placa, String nom, int ed) {
        super(sueldo, grado);
        p = new Persona(nom, ed);
        this.placa = placa;
    }

    public JefePolicia() {
        super();
        this.placa = 0;
    }

    @Override
    public double getSueldo() {
        return this.sueldo;
    }

    @Override
    public String getNombre() {
        return p.nombre;
    }
    
    
    
}
