package SistemaPizzaria;// Gabriel Antonio Gomes de Farias 2@ Periodo BCC manhã
import java.util.Scanner;
public class Main {
    // Scanner para receber dados...
    static Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        Pedido pedido_cliente = null; // pedido do cliente, começa nulo
        boolean confirma; // flag booleana para confirmar escolhas


        System.out.println("Pizzaria do Gab!"); // msg generica menu
        while (true)
        {
            // menu opções
            System.out.println();
            String opcoes = "\n1. Cadastrar Pedido." +
                    "\n2. Adicionar pizza ao pedido.\n3. Calcular Valor total do pedido." +
                    "\n4. Exibir Dados do pedido.\n5. Modificar Informação Cliente\n6. Remover Pizza\n\nS. Sair";
            String escolha = retornaStr(opcoes);
            switch (escolha)
            {
                // cadastrar cliente
                case "1":
                    String cliente_nome = retornaStr("Qual o nome do cliente?");
                    String cliente_telefone = retornaStr("Qual o telefone do cliente?");
                    String cliente_endereco = retornaStr("Qual o endereço do cliente?");
                    System.out.println();
                    System.out.printf("Nome: %s\nTelefone: %s\nEndereço: %s ",
                            cliente_nome,cliente_telefone,cliente_endereco);
                    System.out.println();
                    System.out.println("Confirmar novo pedido?");
                    confirma = retornaBol();
                    if (confirma)
                    {
                        // confirma se os dados estão certos
                        Pessoa cliente = new Pessoa(cliente_nome,cliente_telefone,cliente_endereco);
                        pedido_cliente = new Pedido(cliente);
                    }
                    break;
                case "2":
                    if(pedido_cliente != null)
                    {
                        Pizza pizza_pedido; //
                        String pizza_sabor = retornaStr("Qual o sabor da pizza?");
                        String pizza_tamanho = tamanhoPizza();
                        Double pizza_valor = valorPizza();
                        if(pizza_tamanho.equals("PEQUENA"))
                        {
                            System.out.println("OBS: A pizza pequena custa o valor original.");
                            pizza_valor *= 1;
                        }
                        else if(pizza_tamanho.equals("MEDIA"))
                        {
                            System.out.println("OBS: A pizza média tem um acrescimo de 50% há mais.");
                            // informa o mod do tamanho
                            pizza_valor *= 1.5;
                        }
                        else
                        {
                            System.out.println("OBS: A pizza grande custa o dobro."); // informa o mod adc do tamanho
                            pizza_valor *= 2;
                        }
                        System.out.printf("Adicionar pizza de %s %s com o valor de %s R$?",pizza_sabor,
                                pizza_tamanho.toLowerCase(),pizza_valor);
                        confirma = retornaBol();
                        if(confirma)
                        {
                            System.out.println("Pizza Adicionada!");
                            pizza_pedido = new Pizza(pizza_tamanho,pizza_valor,pizza_sabor);
                            pedido_cliente.adicionarPizza(pizza_pedido);
                        }
                    }
                    else
                    {
                        System.out.println("Erro: Precisa ter um pedido criado para adicionar uma pizza.");
                    }
                    break;
                case "3":
                    if(pedido_cliente != null)
                    {
                        if(pedido_cliente.getPizzas_pedido().size() > 0)
                        {
                            pedido_cliente.calculartotalPedido();
                            pedido_cliente.exibirtotalPedido();
                        }
                        else
                        {
                            System.out.println("Erro: Não há pizzas no pedido...");
                        }
                    }
                    else
                    {
                        System.out.println("Erro: Precisa ter um pedido criado para calcular o valor total.");
                    }
                    break;
                case "4":
                    if(pedido_cliente != null)
                    {
                        if(pedido_cliente.getPizzas_pedido().size() > 0) {
                            pedido_cliente.exibirPedido();
                        }
                        else
                        {
                            System.out.println("Erro: Não pizzas no pedido...");
                            System.out.println();
                        }
                    }
                    else
                    {
                        System.out.println("Erro: Precisa ter um pedido criado para visualizar.");
                    }
                    break;
                case "5":
                    if(pedido_cliente != null)
                    {
                        boolean modificar = true;
                        while (modificar) {
                            pedido_cliente.getCliente().dadosCliente();
                            System.out.println("1. Nome\n2. Telefone\n3. Endereço.\n\nS. Voltar");
                            System.out.println();
                            String alterar = retornaStr("Escolha um opção.");
                            switch (alterar) {
                                case "1":
                                    String novo_nome = retornaStr("Qual o nome do cliente?");
                                    pedido_cliente.getCliente().setNome(novo_nome);
                                    break;
                                case "2":
                                    String novo_telefone = retornaStr("Qual o telefone do cliente?");
                                    pedido_cliente.getCliente().setTelefone(novo_telefone);
                                    break;
                                case "3":
                                    String novo_endereco = retornaStr("Qual o endereço do cliente?");
                                    pedido_cliente.getCliente().setEndereco(novo_endereco);
                                    break;
                                case "s":
                                case "S":
                                    modificar = false; // fecha menu de modificar
                                    break;
                                default:
                                    System.out.println("Opção inválida.");
                                    break;
                            }
                        }
                    }
                    else
                    {
                        System.out.println("Erro: Precisa ter um pedido criado para modificar.");
                    }
                    break;
                case "6":
                    if(pedido_cliente != null)
                    {
                        boolean remover_pizza = true;
                        while (remover_pizza)
                        {
                            if(pedido_cliente.getPizzas_pedido().size() > 0)
                            {
                                int cont = 1;
                                for(Pizza x:pedido_cliente.getPizzas_pedido())
                                {
                                    System.out.printf("%s - Sabor: %s | Valor: %s", cont,x.getSabor(),x.getPreco());
                                    System.out.println();
                                    cont +=1;
                                }

                                    String indice_pizza = retornaStr(
                                            "Coloque o n° da pizza para remover ou S para voltar");
                                    if(indice_pizza.equals("s") || indice_pizza.equals("S"))
                                    {
                                        remover_pizza = false;
                                    }
                                    else
                                    {
                                        // tenta caso de um array out of bounds um string no lugar de indice
                                        try {
                                            // trnasforma em indice
                                            int pizza_indice = Integer.parseInt(indice_pizza)-1;
                                            System.out.println();
                                            System.out.printf("Pizza sabor %s removida!",
                                                    pedido_cliente.getPizzas_pedido().get(pizza_indice).getSabor());
                                            System.out.println();


                                            pedido_cliente.getPizzas_pedido().remove(pizza_indice);
                                        }
                                        catch (Exception e)
                                        {
                                            // erro generico trata o array out of bounds e caso for char
                                            System.out.println("Erro: Não há uma pizza com esse valor");
                                        }
                                    }
                                }
                            else
                            {
                                    System.out.println("Erro: Não ha pizzas no pedido.");
                                    remover_pizza = false;
                            }
                        }

                    }
                    else
                    {
                        System.out.println("Erro: Precisa ter um pedido para modificar.");
                    }
                    break;
                case "s":
                case "S":
                    System.out.println("Adeus!");
                    System.exit(0);
                    // encerra o programa
                default:
                    System.out.println("Opção inválida...");
                    break;
            }
        }
    }
    // Metodos estáticos para facilitar retorno
    static String retornaStr(String pergunta)
    {
        // retorna dado string generico
        System.out.println(pergunta); // pergunta é oq deve aparecer na tela ex."Coloque o nome"/ "Coloque endereço"
        String dado_str;
        System.out.println();
        System.out.print(">> ");
        dado_str = entrada.nextLine();
        return dado_str; // retorna str
    }
    static boolean retornaBol()
    {
        // retorna confirmação generica
        while (true) {
        System.out.println();
        System.out.print("(S/N)>>");
        String escolha = entrada.nextLine();
            switch (escolha) {
                case "s":
                case "S":
                    return true;
                case "n":
                case "N":
                    return false;
                default:
                    System.out.println("Opção inválida");
                    break;
            }
        }
    }
    static String tamanhoPizza()
    {
        // retorna o tamanho da pizza. 3 possiveis
        while (true) {
        System.out.println("1. Pequena | 2. Média | 3. Grande");
        System.out.println("Qual o tamanho da pizza?");
        String tamanho;
        System.out.println();
        System.out.print(">> ");
        tamanho = entrada.nextLine();
            switch (tamanho) {
                case "1":
                    return "PEQUENA";
                case "2":
                    return "MEDIA";
                case "3":
                    return "GRANDE";
                default:
                    System.out.println("Opção inválida");
                    break;
            }
        }
    }
    static Double valorPizza()
    {
        while (true) {
            System.out.println("Qual o valor da pizza?");
            String valor_str;
            double valor;
            System.out.println();
            System.out.print(">> ");
            valor_str = entrada.nextLine();
            try{
                valor = Double.parseDouble(valor_str);
                if(valor > 0) // valor n pode ser negativo
                {
                return valor;
                }
                else
                {
                    System.out.println("Erro: O preço não pode ser negativo...");
                }
            }
            catch (Exception e )
            {
                System.out.println("Por favor insira o valor da pizza...");
                System.out.println();
            }
        }
    }
}
