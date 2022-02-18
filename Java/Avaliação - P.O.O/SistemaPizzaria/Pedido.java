package SistemaPizzaria;
import java.util.ArrayList;
import java.util.Scanner;
public class Pedido {
    private ArrayList<Pizza> pizzas_pedido = new ArrayList<>();
    private Pessoa cliente;
    private Double valorPedido;

    public Pedido(Pessoa cliente) {
        this.cliente = cliente;
    }

    public ArrayList<Pizza> getPizzas_pedido() {
        return pizzas_pedido;
    }



    public Pessoa getCliente() {
        return cliente;
    }

    public Double getValorPedido() {
        return valorPedido;
    }

    public void setValorPedido(Double valorPedido) {
        this.valorPedido = valorPedido;
    }

    void adicionarPizza(Pizza pizza) // adc pizza
    {
        pizzas_pedido.add(pizza);
        System.out.printf("Pizza '%s' adicionada ao pedido!",pizza.getSabor());
    }

    void exibirPedido()
    {
        System.out.println("Dados cliente:");
        System.out.printf("Nome: %s\nTelefone: %s\nEndereço: %s",getCliente().getNome(),getCliente().getTelefone(),
                getCliente().getEndereco());
        System.out.println();
        int cont = 1;
        System.out.println();
        for (Pizza x:getPizzas_pedido())
        {
            System.out.println("N° Pedido: "+cont);
            System.out.println("Sabor: "+x.getSabor());
            System.out.println("Tamanho: "+x.getTamanho());
            System.out.println("Preço: "+x.getPreco());
            System.out.println();
            cont += 1;
        }
    }
    void calculartotalPedido() // calcular
    {
        double total = 0;
        for (Pizza x : getPizzas_pedido()) {
            total += x.getPreco();
        }

        setValorPedido(total);
    }
    void exibirtotalPedido()
    {
        System.out.printf("Total de pizzas: %s",getPizzas_pedido().size());
        System.out.println();
        System.out.printf("O valor total do pedido é %s R$",getValorPedido());
        System.out.println();
    }


}
