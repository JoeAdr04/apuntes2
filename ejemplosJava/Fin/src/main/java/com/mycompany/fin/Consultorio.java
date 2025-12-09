package com.mycompany.fin;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;


public class Consultorio {
    private String medicos;
    private String consultas;

    public Consultorio(String med, String con) {
        this.medicos = med;
        this.consultas = con;
        try{
            File f = new File(this.medicos);
            
            if(!f.exists()){
                ArrayList<Consulta> l = new ArrayList<>();
                
                try(FileWriter nuevo = new FileWriter(this.medicos) ){
                    new Gson().toJson(l, nuevo);
                }
                
              
            }
        }
        catch (Exception e){
            System.out.println(e);
        }
        try{
            File f2 = new File(this.consultas);
            if(!f2.exists()){
                ArrayList<Medico> l2 = new ArrayList<>();
                
                try(FileWriter nuevo2 = new FileWriter(this.medicos) ){
                    new Gson().toJson(l2, nuevo2);
                    System.out.print("asdf");
                }
              
            }
        }
        catch (Exception e){
            System.out.println(e);
        }
    }

 
    
    public List<Medico> leerMedicos(){
        try{
           File arch = new File(this.medicos);
           if (!arch.exists()){
               return new ArrayList<>();
           }
           else{
               Type lista = new TypeToken<List<Medico>>() {}.getType();
               List<Medico> resultado = new Gson().fromJson(new FileReader(this.medicos), lista);
               if (resultado == null) {
                   return new ArrayList<>();
               }
               return resultado;
           }
       }
       catch(Exception e){
           System.out.println(e);
           return new ArrayList<>();
       }
    }
    public List<Consulta> leerConsutas(){
        try{
           File arch = new File(this.consultas);
           if (!arch.exists()){
               return new ArrayList<>();
           }
           else{
               Type lista = new TypeToken<List<Consulta>>() {}.getType();
               List<Consulta> resultado = new Gson().fromJson(new FileReader(this.consultas), lista);
               if (resultado == null) {
                   return new ArrayList<>();
               }
               return resultado;
           }
       }
       catch(Exception e){
           System.out.println(e);
           return new ArrayList<>();
       }
    }
    
    public void modificarM(List<Medico> frat){
        try(FileWriter escritor = new FileWriter(this.medicos)){
            new Gson().toJson(frat, escritor);
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
    
    public void modificarC(List<Consulta> frat){
        try(FileWriter escritor = new FileWriter(this.consultas)){
            new Gson().toJson(frat, escritor);
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
    
    
    public void altaMedico(Medico m){
        List<Medico> todas = this.leerMedicos();
        todas.add(m);
        System.out.println("fraternidad agregada con exito");
        this.modificarM(todas);
    }
    public void altaConsulta(Consulta m){
        List<Consulta> todas = this.leerConsutas();
        todas.add(m);
        System.out.println("fraternidad agregada con exito");
        this.modificarC(todas);
    }
    public void bajaMedico(String x, String y){
        List<Medico> medicos = this.leerMedicos();
        ArrayList<Medico> nuevo = new ArrayList<>();
        for(Medico m : medicos){
            if(!m.getNombreMed().equals(x) && !m.getApmedico().equals(y)){
                nuevo.add(m);
            }
            
        }
        this.modificarM(nuevo);
    }
    
    public void cambia(String m, int d){
        List<Consulta> consultas =this.leerConsutas();
        for(Consulta c : consultas){
            if ((c.getDia() == 25 ||c.getDia() == 31) &&(c.getMes().equals("diciembre") ||c.getMes().equals("diciembre"))){
                c.setDia(d);
                c.setMes(m);
            }
        }
        this.modificarC(consultas);
    }
}
