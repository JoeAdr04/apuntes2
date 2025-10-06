package filaa;


public class Parqueo {
    private int nroVehiculos;
    private double tarifaHora;
    private String[][] vehiculos = new String[50][2];
    private int[][] tiempo = new int[50][2];

    public Parqueo(int nv, double tariho, String[][] v, int[][]t) {
        this.nroVehiculos = nv;
        this.tarifaHora = tariho;
        this.vehiculos = v;
        this.tiempo = t;
    }
    @Override
    public String toString() {
        String cad = "Nrovehiculos: " + nroVehiculos + ", tarifaPorHora: " + tarifaHora + "\n";
        for (int i = 0; i < nroVehiculos-1; i++) {
            if (vehiculos[i][0] != null) {
                cad += "[" + vehiculos[i][0] + "][" + vehiculos[i][1] + "], "
                     + "[" + tiempo[i][0] + "][" + tiempo[i][1] + "]\n";
            }
        }
        return cad;
    }    /*
    def __add__(self, p):
        for i in range(nroVehiculos):
            if (self.__vehiculos[i][0] == p):
                importe = (self.__tiempo[i][1]-self.__tiempo[i][0])*self.__tarifaHora
                print(f"Importe a cancelar: {importe}")
                self.__vehiculos.pop(i)
                self.__tiempo.pop(i)
                break
    */
    
    public double ingreso(){
        double importe = 0.0;
        int horas;
        for(int i=0;i<this.nroVehiculos;i++){
            horas = this.tiempo[i][1]-this.tiempo[i][0];
            importe =importe + horas*this.tarifaHora;
        }
        return importe;
    }
    public double ingreso(int k){
        double importe = 0.0;
        int horas;
        for(int i=0;i<this.nroVehiculos;i++){
            horas = this.tiempo[i][1]-this.tiempo[i][0];
            if(horas == k){
                importe =importe + horas*this.tarifaHora;
            }
        }
        return importe;
    }
}
