package Aula3009;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Agenda agenda = new Agenda();
        agenda.ListarContatos();
        Pessoa p1 = new Pessoa("amangus","sussus","aol@aaa.com");
        agenda.adc(p1);
        agenda.ListarContatos();
    }
}
