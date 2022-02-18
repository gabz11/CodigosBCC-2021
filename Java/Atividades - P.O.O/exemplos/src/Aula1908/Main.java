package Aula1908;
import  java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String nome, titulo, genero, nomealbum;
        int idade, duracaominutos, ano;
        Scanner entrada = new Scanner(System.in);
        System.out.print("\nNome da pessoa\n>> ");
        nome = entrada.nextLine();
        System.out.print("\nIdade da pessoa\n>> ");
        idade = entrada.nextInt();
        Pessoa p1 = new Pessoa(nome, idade);
        System.out.printf("\nNome:%s\nIdade:%s",p1.getNome(),p1.getIdade());
        System.out.print("\nNome da música\n>> ");
        entrada.nextLine();
        titulo = entrada.nextLine();
        System.out.print("\nDuração da música(minutos)\n>> ");
        duracaominutos = entrada.nextInt();
        Musica m1 = new Musica(titulo, duracaominutos);
        System.out.printf("\nTitulo:%s\nDuração(Minutos):%s", m1.getTitulo(), m1.getDuracaominutos());
        m1.TocarMusica();
        System.out.print("Coloque o genero\n>> ");
        entrada.nextLine();
        genero = entrada.nextLine();
        System.out.print("Coloque o ano\n>> ");
        ano = entrada.nextInt();
        System.out.println("Coloque o nome do album\n>> ");
        nomealbum = entrada.nextLine();
    }
}
