/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package relaciones;
import java.util.ArrayList;
/**
 *
 * @author Jaeger
 */
public class Test {
    private ArrayList<Cosas>lista = new ArrayList();

    public Test() {
    }
    
    public void agrega(Cosas x){
        lista.add(x);
    }

    @Override
    public String toString() {
        return "Test{" + "lista=" + this.desplegar() + '}';
    }
    
    public String desplegar(){
        String cad = "";
        for(Cosas c:lista){
            cad = cad+ "{Nombre:"+c.getNombre()+", codigo: "+c.getCodigo()+"}\n";
        }
        return cad;
    }
    
}
