package Aula0109;

public class ImovelNovo extends Imovel{
    private Double preco = this.valor * 1.1;
    public Double getPreco() {
        return preco;
    }
    public void setPreco(Double valor) {
        this.preco = valor * 1.1;
    }

    @Override
    public Double getValor() {
        return super.getValor();
    }

    @Override
    public void setValor(Double valor) {
        super.setValor(valor);
    }
}
