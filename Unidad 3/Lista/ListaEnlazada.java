package com.mx.ux.unidad3.lista.simple;

public class ListaEnlazada {

    // Referencia al primer nodo de la lista
    Nodo cabeza;

    public ListaEnlazada(){
        this.cabeza = null;
    }

    public void insertarAlInicio (int nuevoDato){

        // Creamos un nuevo nodo
        Nodo nuevoNodo = new Nodo(nuevoDato);
        nuevoNodo.siguiente = cabeza;

        cabeza = nuevoNodo;
        System.out.println("Insertando al inicio: " + nuevoDato);
    }

    public void insertarAlFinal (int nuevoDato){

        Nodo nuevoNodo = new Nodo(nuevoDato);

        // Si la lista esta vacia el nuevo nodo es la cabeza
        if(cabeza == null){
            cabeza = nuevoNodo;
            System.out.println("Insertado al final (Lista vacia)"+ nuevoDato);
            return;
        }

        // Si la lista no esta vacia, recorrer hasta el ultimo nodo
        Nodo actual = cabeza;
        while (actual.siguiente != null) {
            actual = actual.siguiente;
        }
        // el ultimo nodo apuntando al nuevo nodo
        actual.siguiente = nuevoNodo;
        System.out.println("Insertado al fina: " + nuevoDato);

    }

    public void imprimirLista(){
            Nodo actual = cabeza;
            System.out.println("Lista simple:");

            while (actual != null) {
                System.out.println(actual.dato + " -> ");
                actual = actual.siguiente;
            }

            System.out.println("Null");
    }
}
