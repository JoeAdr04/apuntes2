package com.mycompany.archivos;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class ArchivoLibro {
    Scanner te = new Scanner(System.in);
    private String nombre;
    private Gson gson = new GsonBuilder().setPrettyPrinting().create();
    
    public ArchivoLibro(String nomb) {
        this.nombre = nomb;
        try{
            File a = new File(this.nombre);
            if(!a.exists()){
                ArrayList<Libro> list = new ArrayList<>();
                try(FileWriter nuevo = new FileWriter(this.nombre)){
                    gson.toJson(list, nuevo);
                }
            }
        }
        catch (IOException e){
            System.out.print(e);
        }
        
    }
    public List<Libro>leer(){
        try{
            File arch = new File(this.nombre);
            if(!arch.exists()){
                return new ArrayList<>();
            }
            else{
                   Type lista = new TypeToken<List<Libro>>() {}.getType();
                   List<Libro> salida = this.gson.fromJson(new FileReader(this.nombre), lista);
                   if (salida == null){
                       System.out.println("la salida es vacia o null");
                       return new ArrayList<>();
                   }
                   return salida;  
            }
        }
        catch(IOException x){
            System.out.println(x);
            return new ArrayList<>();
        }
    }
    public void modificar(List<Libro> libros){
        try(FileWriter nuevo = new FileWriter(this.nombre)){
            gson.toJson(libros, nuevo);
        }
        catch(IOException x){
            System.out.println(x);  
        }
    }
    
    public void agregarLibro(Libro lib){
        List<Libro> libros = this.leer();
        libros.add(lib);
        this.modificar(libros);
    }
    public void eliminarPorAutor(String autor){
        List<Libro> libros = this.leer();
        ArrayList<Libro> nuevo = new ArrayList<>();
        for(Libro l:libros){
            if(!l.getAutor().equals(autor)){
                nuevo.add(l);
            }
        }
        if(libros.size() != nuevo.size()){
            System.out.println("Libro eliminado con exito");
        }
        this.modificar(nuevo);
    }
    public void editarAutor(String aut){
        List<Libro> libros = this.leer();
        ArrayList<Libro> nuevo = new ArrayList<>();
        for(Libro l:libros){
            if((l.getAutor()).equals(aut)){
                System.out.println("ingresa autor:");
                String a = te.next();
                l.setAutor(a);
                nuevo.add(l);
            }
            else{
                nuevo.add(l);
            }
        }
        this.modificar(nuevo);
    }
    
}
