package Aula1609;

public class Pizza {
    public String sabor;

    public Pizza(String sabor) {
        this.sabor = sabor;
    }

    public String getSabor() {
        return sabor;
    }

    public void setSabor(String sabor) {
        this.sabor = sabor;
    }
    public String mostrarMensagem() {
        String pizza = "Pizza do tipo "+this.sabor;
        return pizza;
    }
}
