package com.mycompany.examenfinal;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;


public class ArchivoFraternidad {
    private String nombre;

    public ArchivoFraternidad(String nombre) {
        this.nombre = nombre;
        try{
            File f = new File(this.nombre);
            if(!f.exists()){
                ArrayList<Fraternidad> l = new ArrayList<>();
                try(FileWriter nuevo = new FileWriter(this.nombre)){
                    new Gson().toJson(l, nuevo);
                }
            }
        }
        catch (Exception e){
            System.out.println(e);
        }
    }

    public ArchivoFraternidad() {
        this.nombre = "frate.json";
    }
    
    public List<Fraternidad> leerTodo(){
        try{
           File arch = new File(this.nombre);
           if (!arch.exists()){
               return new ArrayList<>();
           }
           else{
               Type lista = new TypeToken<List<Fraternidad>>() {}.getType();
               List<Fraternidad> resultado = new Gson().fromJson(new FileReader(this.nombre), lista);
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
    
    public void modificar(List<Fraternidad> frat){
        try(FileWriter escritor = new FileWriter(this.nombre)){
            new Gson().toJson(frat, escritor);
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
    
    public void promedioEdad(String x){
        List<Fraternidad> todas = this.leerTodo();
        for (Fraternidad f : todas){
            int suma = 0, cont = 0;
            for (Danzarin d: f.getD()){
                if(d.getGenero().equals(x)){
                    suma = suma +d.getEdad();
                    cont ++;
                }
            }
            System.out.println("promedio de edad de la fraternidad "+f.getNombre());
            System.out.println(suma/cont);
        }
    }
    public void eliminarPersona(String nom){
        List<Fraternidad> todas = this.leerTodo();
        ArrayList<Danzarin> nuevo = new ArrayList<>();
        for(Fraternidad f: todas){
            for(Danzarin d: f.getD()){
                if(!d.getNombre().equals(nom)){
                    nuevo.add(d);
                }
            }
            f.setD(nuevo);
        }
        this.modificar(todas);
    }
    
    public void mostrarParticipaciones(String x){
        List<Fraternidad> todas = this.leerTodo();
        for(Fraternidad f: todas){
            if(f.getNombre().equals((x))){
                int max = 0;
                for(Danzarin d: f.getD()){
                    if(d.getNroParticiopaciones() >max){
                        max = d.getNroParticiopaciones();
                    }
                }
                for(Danzarin d: f.getD()){
                    if(d.getNroParticiopaciones() ==max){
                        System.out.println(d);
                    }
                }
            }
        }
    }
    
    public void agregarFraternidad(Fraternidad f){
        List<Fraternidad> todas = this.leerTodo();
        todas.add(f);
        System.out.println("fraternidad agregada con exito");
        this.modificar(todas);
    }
    
}
