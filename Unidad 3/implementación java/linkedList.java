public class HistorialTransacciones {
 
    public static void main(String[] args) {
 
        LinkedList<String> historial = new LinkedList<>();
 
        System.out.println("Iniciamos el historial de transacciones");
 
        ListIterator<String> iterador = historial.listIterator();
 
        iterador.add("Accion 1: Crear Documento");
        iterador.add("Accion 2: Escribir Titulo");
        iterador.add("Accion 3: Insertar Imagen");
 
        System.out.println("Historial Completo  " + historial);
 
        System.out.println("Estado Actual (Accion mas reciente):" +
                historial.getLast());
 
        if (iterador.hasPrevious()) {
            String accionDes = iterador.previous();
            System.out.println("UNDO" + accionDes);
        }
 
        if (iterador.hasPrevious()) {
            String accionDes = iterador.previous();
            System.out.println("UNDO" + accionDes);
        }
 
        System.out.println("Estado actual " + iterador.next());
 
        if(iterador.hasNext()){
            String accionRes = iterador.next();
            System.out.println("REDO"+ accionRes);
        }
        System.out.println("Estado actual " + historial.get(iterador.previousIndex()));
 
    }
}