package com.mx.ux.unidad3.lista.simple;

public class testLista {

    public static void main(String[] args) {
        // Crear una istancia de lista enlazada
        ListaEnlazada lista = new ListaEnlazada();

        System.out.println("Insertar nuevos datos");
        lista.insertarAlInicio(10);
        lista.insertarAlInicio(20);

        System.out.println("Insertar datos al final: ");
        lista.insertarAlFinal(30);
        lista.insertarAlFinal(40);

        lista.insertarAlInicio(50);

        lista.imprimirLista();

    }
}
