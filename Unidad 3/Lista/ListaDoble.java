public class EjemploListaDoble {
 
    public static void main(String[] args) {
 
        ListaDoble lista = new ListaDoble();
        lista.agregar(1);
        lista.agregar(2);
        lista.agregar(3);
        lista.agregar(4);
 
        System.out.println("Recorremos hacia adelante");
        lista.imprimirHaciaAdelante();
 
        System.out.println("Recorremos hacia atras");
        lista.imprimirHaciaAtras();
    }
}
 
 
class Nodo {
 
    int dato;
    Nodo siguiente;
    Nodo anterior;
 
    public Nodo(int dato) {
        this.dato = dato;
        this.anterior = null;
        this.siguiente = null;
    }
}
 
class ListaDoble {
 
    Nodo cabeza; // referencia al primer nodo
    Nodo cola; // referencia al ultimo nodo
 
    public ListaDoble() {
        this.cabeza = null;
        this.cola = null;
    }
 
    // Construir un mmetodo para agregar un nodo al final de la lista
    public void agregar(int dato) {
 
        Nodo nuevoNodo = new Nodo(dato);
 
        if (cabeza == null) {
            cabeza = nuevoNodo;
            cola = nuevoNodo;
            return;
        }
 
        cola.siguiente = nuevoNodo;
        nuevoNodo.anterior = cola;
        cola = nuevoNodo;
    }
 
    public void imprimirHaciaAdelante() {
        Nodo actual = cabeza;
        while (actual != null) {
            System.out.println(actual.dato + "<->");
            actual = actual.siguiente;
        }
        System.out.println("null");
    }
 
    public void imprimirHaciaAtras() {
        Nodo actual = cola;
        while (actual != null) {
            System.out.println(actual.dato + "<->");
            actual = actual.anterior;
        }
        System.out.println("null");
    }
 
 
}