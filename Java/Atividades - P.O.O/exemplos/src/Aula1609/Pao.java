package Aula1609;

public class Pao {
    public String tipo;

    public Pao(String tipo) {
        this.tipo = tipo;
    }


    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public String mostrarMensagem() {
        String pao = "Pão do tipo "+this.tipo;
        return pao;
    }
}
