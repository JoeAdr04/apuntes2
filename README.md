

# Diagrama de la clase Persona

```mermaid
classDiagram
    class Persona {
        - String nombre
        - int edad
        - String direccion
        + Persona(String nombre, int edad, String direccion)
        + getNombre() String
        + getEdad() int
        + getDireccion() String
        + setNombre(String nombre) void
        + setEdad(int edad) void
        + setDireccion(String direccion) void
        + toString() String
    }
