package SistemaPizzaria;
public class Pizza {
    private String tamanho; // PEQUENA | MEDIA | GRANDE
    private Double preco;
    private String sabor;

    public Pizza(String tamanho, Double preco, String sabor)
    {
        this.tamanho = tamanho;
        this.preco = preco;
        this.sabor = sabor;
    }


    public String getTamanho() {
        return tamanho;
    }


    public Double getPreco() {
        return preco;
    }


    public String getSabor() {
        return sabor;
    }




}
