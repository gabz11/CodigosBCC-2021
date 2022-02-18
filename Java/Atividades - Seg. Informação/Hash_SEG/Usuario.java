package Hash_SEG;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Usuario {

    String nome;
    String senha;



    public Usuario(String nome, String senha) {
            this.nome = nome;
            this.senha = senha;
    }


    public static void AutenticarUsuario(String nome, String senha, String[] lista_primitiva) {
        ArrayList<String> lista = new ArrayList<>();
        lista.addAll(Arrays.asList(lista_primitiva));
        boolean autenticou = false;
        for (int i = 0; i <= lista.size() - 1; i++) {
            String[] novo = lista.get(i).split(";");

            if (nome.equals(novo[0]) && (senha.equals(novo[1]))) {
                autenticou = true;
                break;
            }
        }
        if(!autenticou)
        {
            System.out.println("Usuário ou senha incorreto.");
        }
        else
        {
            System.out.println("Usuário autenticado!");
        }
    }
}
