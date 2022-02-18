package Aula1609;

public class Carne {
    public String corte;

    public Carne(String corte) {
        this.corte = corte;
    }

    public String getCorte() {
        return corte;
    }

    public void setCorte(String corte) {
        this.corte = corte;
    }

    public String mostrarMensagem() {
        String carne = "Carne do tipo "+this.corte;
        return carne;
    }
}
