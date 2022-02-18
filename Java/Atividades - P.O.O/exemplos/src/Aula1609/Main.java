package Aula1609;

public class Main {
    public static void main(String[] args) {
        Pao p1 = new Pao("Bacchiata");
        Pizza pi1 = new Pizza("Miojo");
        Carne c1 = new Carne("Cachorro");
        Comida c = new Comida();
        c.assar(p1);
        c.assar(pi1);
        c.assar(c1);
        EsporteRadical e1 = new EsporteRadical();
        e1.Manobras();
        Skate sk8 = new Skate();
        sk8.Manobras();
    }
}
