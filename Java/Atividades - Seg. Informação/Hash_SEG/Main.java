package Hash_SEG;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {


    public static void main(String[] args) throws Exception {
        LerArquivo lerArquivo = new LerArquivo();
        EscreverArquivo escreverArquivo = new EscreverArquivo();
        Scanner input = new Scanner(System.in);
        Hash hash = Hash.getInstance();
        BruteCrack forcabruta = new BruteCrack();
        while (true) {
            System.out.println("-=-=-=-=-=-=-=-=-=-=-=-");
            System.out.println("1. Cadastrar usuário.");
            System.out.println("2. Autenticar usuário.");
            System.out.println("3. Ataque Força Bruta.");
            System.out.println("S. Sair");
            System.out.println("-=-=-=-=-=-=-=-=-=-=-=-");

            String escolha = input.nextLine();
            String[] usuarios;
            switch (escolha) {
                case "1" -> {
                    usuarios = lerArquivo.AbrirArquivo();
                    for (String x : usuarios) {
                        System.out.println(x);
                    }

                    System.out.println("Digite seu nome: ");
                    String nome = input.nextLine();
                    System.out.println("Digite sua senha: ");
                    String senha = input.nextLine();
                    if (nome.length() == 4 && senha.length() == 4) {
                        senha =  hash.toString(senha);
                        String envio = nome + ";" + senha;
                        escreverArquivo.escreverLinha(envio);
                        System.out.println("Cadastro com sucesso");
                    }
                    else
                    {
                        System.out.println("Senha ou usuario deve possuir 4 caracteres");
                    }
                    usuarios = lerArquivo.AbrirArquivo();
                    for (String x : usuarios) {
                        System.out.println(x);
                    }
                }

                case "2" -> {
                    System.out.println("Digite seu nome: ");
                    String nome = input.nextLine();
                    System.out.println("Digite sua senha: ");
                    String senha = input.nextLine();
                    senha = hash.toString(senha);
                    System.out.println("Entrada Autenticação:");
                    System.out.println(nome);
                    System.out.println(senha);
                    String[] listaUsuarios;
                    listaUsuarios = lerArquivo.AbrirArquivo();

                    Usuario.AutenticarUsuario(nome, senha, listaUsuarios);
                }
                case "3" ->
                        {
                            String advinha;
                            usuarios = lerArquivo.AbrirArquivo();
                            ArrayList<String> usuarios_array = new ArrayList<>();
                            usuarios_array.addAll(Arrays.asList(usuarios));
                            int contas_restantes = usuarios_array.size();
                            if (usuarios_array.size() > 0) {
                                long tempo_inicio = System.currentTimeMillis(); // tempo atual em ms
                                for (int i = 0; i <= usuarios_array.size() - 1; i++) {
                                    String[] usuario = usuarios_array.get(i).split(";");
                                    System.out.println();
                                    System.out.printf("Senhas Restantes: %s", contas_restantes);
                                    System.out.println();
                                    System.out.printf("Quebrando senha de \"%s\"", usuario[0]);
                                    System.out.println();
                                    advinha = forcabruta.crack(usuario[1]);
                                    System.out.println("Login:");
                                    System.out.printf("Nome: %s", usuario[0]);
                                    System.out.println();
                                    System.out.printf("Senha crackeada: %s", advinha);
                                    System.out.println();
                                    contas_restantes -= 1;
                                }
                                long tempo_final = System.currentTimeMillis();
                                long total = tempo_final - tempo_inicio;
                                long total_seg = total/1000;
                                System.out.println();
                                System.out.printf("%s ms (aproximadamente %s segundo(s)) para crackear %s senha(s)",
                                        total,total_seg,usuarios_array.size());
                                System.out.println();
                            }
                            else{
                                System.out.println("Não há usuários cadastros para crackear");
                            }
                        }
                case "s","S" -> System.exit(0);
                default -> System.out.println("Escolha inválida.");
            }
        }
    }
}


/*
String filmename = "autenticacao.txt";

BufferedReader br = new BufferedReader(
                       new InputStreamReader(
                           new FileInputStream(filename), "UTF-8"));

String line;

while ( (line = br.readLine()) != null )
{
    line.split(";")...
}
br.close();
 */
