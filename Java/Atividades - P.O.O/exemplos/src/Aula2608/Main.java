package Aula2608;
//import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        String prompt, nomefilme, anofilme;

        boolean flag;

        ArrayList<Filme> filmes = new ArrayList<>();
        System.out.print("Filmes | 26.08");
        System.out.print("\n1. Adicionar Filme\n2. Exibir");
        while (true) {
            System.out.print("\n>> ");
            prompt = entrada.next();
            entrada.nextLine();
            switch (prompt) {
                case "1":
                    flag = true;
                    while (flag) {
                        System.out.print("\nNome do Filme\n>>");
                        nomefilme = entrada.nextLine();
                        System.out.print("\nAno do Filme\n>> ");
                        anofilme = entrada.nextLine();
                        if (!nomefilme.isBlank() && !anofilme.isBlank()) {
                            Filme filme = new Filme(nomefilme, anofilme);
                            filmes.add(filme);
                            System.out.print("Filme adicionado");
                            flag = false;
                        } else {
                            System.out.print("\nNão pode deixar titúlo ou ano vázios...");
                            flag = false;
                        }
                    }
                    break;
                case "2":
                    for (Filme x : filmes) {
                        System.out.printf("\nTitulo: '%s' Ano: '%s'", x.getTitulo(), x.getAnoLancamento());
                    }
                    break;
                case "s":
                case "S":
                    System.out.println("Adeus!");
                    System.exit(0);
                default:
                    System.out.print("\nOpção inválida...");
                    break;
            }
            }
        }
}
