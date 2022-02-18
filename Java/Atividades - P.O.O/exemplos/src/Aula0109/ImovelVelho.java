package Aula0109;

public class ImovelVelho extends Imovel{
    private Double preco = this.valor * 0.9;
    public Double getPreco() {
        return preco;
    }
    public void setPreco(Double valor) {
        this.preco = valor * 0.9;
    }
}
