import java.util.ArrayDeque;   

public class ejemploStack{

    public static void main(string[]args){

        ArrayDeque<integer>stack = new ArrayDeque<>();
        stack.push(e: 100);
        stack.push(e: 200);
        stack.push(e: 300);

        system.out.println("Contenido de la pila: " + stack);

        int elemento = stack.pop();
        system.out.println("Elemento: " + elemento);
    }
}