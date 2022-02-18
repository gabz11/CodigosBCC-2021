package Testes;

import java.util.Random;

public class Aleatorio {
    Random random = new Random();
    String[] objetoaleatorio = {"penis","vassoura","amogus"};
    String[] lugaraleatorio = {"rua bolsonaro","cracolandia","amogusverse"};

    String RetornaAleatoriedade(String nome_jogador,String texto)
    {
        texto = texto.replace("NOME_JOGADOR",nome_jogador);
        texto = texto.replace("OBJETO_ALEATORIO", objetoaleatorio[random.nextInt(objetoaleatorio.length)]);
        texto = texto.replace("LUGAR_ALEATORIO", lugaraleatorio[random.nextInt(objetoaleatorio.length)]);
        return texto;
    }
}
