package Aula0109;
import java.util.ArrayList;

public class Pedido {
    private String nomeCliente;
    private String telefone;
    private String endereco;
    private ArrayList<Pizza> pizzas;

    public String getNomeCliente() {
        return nomeCliente;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public ArrayList<Pizza> getPizzas() {
        return pizzas;
    }

    public void setPizzas(ArrayList<Pizza> pizzas) {
        this.pizzas = pizzas;
    }

    public void addPizza(Pizza pizza) {
        this.pizzas.add(pizza);
    }

    public Pedido(String nomeCliente, String telefone, String endereco) {
        this.nomeCliente = nomeCliente;
        this.telefone = telefone;
        this.endereco = endereco;
        this.pizzas = new ArrayList<Pizza>();
    }
    public void mostrarPedido() {
        System.out.printf("Cliente: %s\nTelefone: %s\nEndereço: %s",nomeCliente,telefone,endereco);
        for(Pizza pizza:pizzas) {
            System.out.printf("\nSabor: %s\nTamanho: %s", pizza.getSabor(), pizza.getTamanho());
        }
    }
}
