package com.mycompany.archivos;


public class Libro {
    private String autor;
    private String titulo;
    private int anio;

    public Libro(String autor, String titulo, int anio) {
        this.autor = autor;
        this.titulo = titulo;
        this.anio = anio;
    }

    public Libro(String autor) {
        this.autor = autor;
    }

    public String getAutor() {
        return autor;
    }

    public String getTitulo() {
        return titulo;
    }

    public int getAnio() {
        return anio;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setAnio(int anio) {
        this.anio = anio;
    }

    @Override
    public String toString() {
        return "Libro{" + "autor=" + autor + ", titulo=" + titulo + ", anio=" + anio + '}';
    }
    
}
