// Gabriel Farias || exemplo 6 || operadores de igualdade e relacionais
package exemplo1; // nome do pacote
import java.util.Scanner; // importa Scanner

public class exemplo6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); // cria Scanner "entrada"
        int num1, num2; // variaveis inteiras
        String prompt = "Digite um número aqui\n>> "; // variavel String do prompt
        System.out.print(prompt); // imprime prompt
        num1 = entrada.nextInt(); // atribui o valor do inteiro num1 para Scanner "entrada"
        System.out.print(prompt); // imprime prompt
        num2 = entrada.nextInt(); //atribui o valor inteiro num2 para Scanner "entrada"

        if(num1 < num2) {
            System.out.printf("%d%s%d", num1," < ",num2);
        } // Operador de igualdade compara se num1 é menor q num2

        else if(num1 == num2) {
            System.out.printf("%d%s%d", num1," = ",num2);
        } // Operador de igualdade compara se num1 é menor q num2
        else {
            System.out.printf("%d%s%d", num1," > ",num2);
        } // podemos deduzir se num1 n for menor ou igual num2, ele sera maior
    } // fim do metodo MAIN
} // fim da classe "exemplo 6"
