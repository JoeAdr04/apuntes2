package filaa;

public class FilaA {

    public static void main(String[] args) {
        String[][] vehiculos = {
            {"1245axd", "Luis Jairo"},
            {"3456pib", "Marcia Lira"},
            {"2576jux", "Pablo Rubio"},
            {"3221lip", "Rosa Jux"},
            {"3456kik", "Saul Lopez"}
        };
        int[][] tiempo = {
            {2, 5},
            {9, 12},
            {10, 12},
            {10, 13},
            {10, 11}
        };
        System.out.println(vehiculos.length);
        Parqueo p = new Parqueo(5, 3, vehiculos, tiempo);

        // Simula el operador +
        // p + "2576jux"
        
        System.out.println(p);

        // Sobrecarga de métodos
        System.out.println("Ingreso total: " + p.ingreso());
        System.out.println("Ingreso de vehiculos con 3 horas: " + p.ingreso(3));
        
        // -------------------- Pregunta 3 --------------------
        Peluqueria p1 = new Peluqueria(5000, "Smart Cut", "Vin Disel");
        Peluqueria p2 = new Peluqueria();
        Salteñeria s = new Salteñeria(4000, "Castor", "David Castro", "Av Buenos Aires");
        Panaderia pa1 = new Panaderia();
        Panaderia pa2 = new Panaderia(2000, "Don Pepe", "Jose Martines");

        Negocio[] todos = {p1, p2, s, pa1, pa2};

        // Comparaciones
        for (int i = 0; i < todos.length; i++) {
            for (int j = i + 1; j < todos.length; j++) {
                todos[i].compara(todos[j]);
            }
        }

        // Mostrar negocio con más capital
        double may = 0;
        for (Negocio n : todos) {
            if (n.getCapital() > may) {
                may = n.getCapital();
            }
        }

        for (Negocio n : todos) {
            if (n.getCapital() == may) {
                System.out.println("Negocio con mas capital:\n" + n);
            }
        }
    }
}
    
    
    
