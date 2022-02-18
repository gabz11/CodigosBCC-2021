package Testes;

public class ItemArma {
    String nome;
    int dano;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getDano() {
        return dano;
    }

    public void setDano(int dano) {
        this.dano = dano;
    }

    public ItemArma(String nome, int dano)
    {
        this.nome = nome;
        this.dano = dano;
    }
}
