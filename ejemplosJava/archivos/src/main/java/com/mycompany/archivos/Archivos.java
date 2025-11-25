/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.archivos;

import com.google.gson.Gson;

public class Archivos {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        ArchivoLibro arch = new ArchivoLibro("biblioteca.json");
        Libro lib = new Libro("yo", "la vida es una referencia", 2020);
        //arch.agregarLibro(lib);
        //arch.eliminarPorAutor("yo");
        arch.editarAutor("yo");
        System.out.println(arch.leer());
    }
}
