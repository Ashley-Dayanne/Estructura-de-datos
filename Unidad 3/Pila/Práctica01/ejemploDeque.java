import java.util.Deque;
import java.util.ArrayDeque;

public class EjemploDeque {
    public static void main(String[].args){
        Deque<String> deque = new.ArrayDeque<>();
        deque.addFirst("e: 1");
        deque.addLast("e: 2");
        deque.addFirst("e: 3");
        
        system out.println("Contenido del deque: " + deque);

        string primero= deque.removeFirst();
        system.out.println(primero);

        string ultimo = deque.removeLast();
        system.out.println(ultimo);

        system.out.println("Contenido Actual: " + deque);
    }
}