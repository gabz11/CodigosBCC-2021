package Aula1908;

public class Restaurante {
    private String nome;
    private String tipoculinaria;
    private String tipoambiente;
    private int faixapreco;
    private boolean sanitizado;

    public String getNome() {
        return this.nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getTipoculinaria() {
        return this.tipoculinaria;
    }
    public void setTipoculinaria(String tipoculinaria) {
        this.tipoculinaria = tipoculinaria;
    }

    public String getTipoambiente() {
        return this.tipoambiente;
    }
    public void setTipoambiente(String tipoambiente) {
        this.tipoambiente = tipoambiente;
    }

    public int getFaixapreco() {
        return this.faixapreco;
    }
    public void setFaixapreco(int faixapreco) {
        this.faixapreco = faixapreco;
    }

    public boolean getSanitizado() {
        return this.sanitizado;
    }
    public void setSanitizado(boolean sanitizado) {
        this.sanitizado = sanitizado;
    }
}
