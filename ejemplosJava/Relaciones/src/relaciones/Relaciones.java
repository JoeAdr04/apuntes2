package relaciones;

public class Relaciones {

    public static void main(String[] args) {
        // TODO code application logic here
        Test t =new Test();
        System.out.println(t);
        Cosas c1 = new Cosas("compu", 1234);
        Cosas c2 = new Cosas("celu", 345);
        Cosas c3 = new Cosas("casa", 4334);
        Cosas c4 = new Cosas("persona", 1234);
        t.agrega(c1);
        t.agrega(c2);
        t.agrega(c3);
        t.agrega(c4);
        System.out.println(t);
    }
    
}
