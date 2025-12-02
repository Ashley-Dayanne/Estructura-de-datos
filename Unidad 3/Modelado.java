public class Torneo {

    public void inscripcionEquipo() {
        System.out.println("Jugador inscrito al equipo de voleibol");
    }

    public void inscripcionTorneo() {
        System.out.println("Jugador inscrito en el torneo");
    }

    public double pagoInscripcion() {
        return 800.00;
    }

    public int calcularHorasEntrenamiento(int horasPorDia, int diasSemana) {
        return horasPorDia * diasSemana;
    }


    public static void main(String[] args) {

        Torneo jugador = new Voleibol();
        jugador.inscripcionEquipo();
        jugador.inscripcionTorneo();
        System.out.println("Pago de inscripción: " + jugador1.pagoInscripcion());
        System.out.println("Horas de entrenamiento: " + jugador1.calcularHorasEntrenamiento(2, 4));
        System.out.println("******************************************************");

        Torneo jugador2 = new Voleibol();
        jugador2.inscripcionEquipo();
        jugador2.inscripcionTorneo();
        System.out.println("Pago de inscripción: " + jugador2.pagoInscripcion());
        System.out.println("Horas de entrenamiento: " + jugador2.calcularHorasEntrenamiento(1, 5));
        System.out.println("******************************************************");
    }
}
