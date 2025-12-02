public class Alumno{

}
public void inscripcionCurso(){
    System.out.println("El alumno se ha inscrito al curso");
}
public void inscripcionTaller(){
    System.out.println("Alumno inscrito al taller de bases de datos");
}
public double pagoMensualidad(){
    return 1500.00;
}
public int calcularHorasEstudio(int horasPorDia, int diasSemana) {
    return horasPorDia * diasSemana;

public static void main(String[] args){

    //Crear un objeto de la clase alumno
    Alumno alumno = new.Alumno();
    alumno.inscripcionCurso();
    alumno.inscripcionTaller();
    System.out.println("Mensualidad: " * alumno.pagoMensualidad());
    System.out.println("Horas de estudio: " + alumno.calcularHorasEstudio(horasPorDia: 1, diasSemana: 5));
    System.out.println("******************************************************");

    //Crear un segundo alumno
    Alumno alumno2 = new.Alumno();
    alumno2.inscripcionCurso();
    alumno2.pagoMensualidad();
    alumno2.inscripcionTaller();    
    System.out.println("Horas de estudio: " + alumno.calcularHorasEstudio(horasPorDia: 1, diasSemana: 5));
    System.out.println("******************************************************");
}
