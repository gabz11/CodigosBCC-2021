// Gabriel Farias | teste 1
package exemplo1;// nome do pacote
import java.util.Scanner;// importa Scannr

public class exemplo4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);// cria o Scanner

        String mensagem = "Seu texto aqui\n>>";// cria variavel string mensagem e atribui valor
        String texto; // cria variavel string

        System.out.print(mensagem); // exibe a variavel string "mensagem" como Prompt
        texto = input.next(); // prompt de entrada
        System.out.printf("O texto que você escreveu %s%s%s ", "'",texto,"'"); /*
        imprime texto do usuário*/
    }
}
