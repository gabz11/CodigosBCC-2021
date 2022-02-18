// Gabriel Farias || java: como programar || soma de 3 números
package exemplo1; // nome do pacote
import java.util.Scanner; // importa scanner

public class exemplo5 {
    public static void main(String[] args) {
    // cria um novo scanner
    Scanner entrada = new Scanner(System.in); // cria uma variavel scanner "entrada"
    String prompt = "Digite um número\n>> "; // cria uma String "prompt"
    int num1 , num2, num3, soma;// cria 4 variaveis inteiras
    System.out.printf("\n%s", prompt); // print imprime variavel prompt
    num1 = entrada.nextInt(); // chama a variavel Scanner "entrada" pedindo um inteiro
    System.out.printf("\n%s", prompt); // imprime prompt
    num2 = entrada.nextInt(); // 2o numero
    System.out.printf("\n%s", prompt); // imprime prompt
    num3 = entrada.nextInt(); // 3o numero
    soma = num1 + num2 + num3; // variavel soma consiste na soma das variaves "num1" + "num2" + "num3"
    System.out.printf("Sua soma é :%d", soma); // imprime uma mensagem exibindo a variaverl soma
    } // fim do metodo main
} // fim da classe
