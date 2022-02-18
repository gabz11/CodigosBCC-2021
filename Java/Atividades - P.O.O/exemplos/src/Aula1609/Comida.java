package Aula1609;

public class Comida {
    public void assar(Pizza p) {
        System.out.println("Assando "+p.mostrarMensagem());
    }
    public void assar(Pao p) {
        System.out.println("Assando "+p.mostrarMensagem());
    }
    public void assar(Carne c) {
        System.out.println("Assando "+c.mostrarMensagem());
    }
}
