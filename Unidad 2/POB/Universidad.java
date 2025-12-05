package com.mx.curso.poo;

public class Universidad {

    public static void main(String[] args) {

        //Crear un objeto de la clase Alumno
        Alumno alumno = new Alumno();
        alumno.incripcionCurso();
        alumno.inscripcionTaller();
        System.out.println("Mensualidad:  " + alumno.pagoMensualidad());
        System.out.println("Horas de estudio: "
                +  alumno.calcularHorasEstudio(1,5));
        System.out.println("********************************");

        //Crear un segundo alumno
        Alumno alumno2 = new Alumno();
        alumno2.incripcionCurso();
        alumno2.pagoMensualidad();
        alumno2.inscripcionTaller();
        System.out.println("Horas de estudio: "
                +  alumno.calcularHorasEstudio(1,5));

        //Invocar al metodo sin crear un objeto de la clase Docente
        Docente.asignarCalificacion();

    }
}
