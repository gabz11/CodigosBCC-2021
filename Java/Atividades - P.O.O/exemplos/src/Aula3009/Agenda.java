package Aula3009;

import java.util.ArrayList;

public class Agenda {
    ArrayList<Pessoa> contatos;

    public Agenda() {
        this.contatos = new ArrayList<>();
    }

    public void adc(Pessoa contato) {
        contatos.add(contato);
    }
    public void ListarContatos() {
        if(contatos.size() == 0) {
            System.out.println("0 Contatos");
        }
        else {
            for (Pessoa contato : contatos) {
                System.out.printf("Nome: %s || Sobrenome: %s || E-mail: %s",contato.getNome(), contato.getSobrenome(),contato.getEmail());
            }
        }
    }
}
