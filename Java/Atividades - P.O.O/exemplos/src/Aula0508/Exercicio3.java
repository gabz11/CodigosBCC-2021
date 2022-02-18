// Gabriel Farias | Exemplo 3 | Aritmética
package Aula0508;
import java.util.Scanner; // entrada

public class Exercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); // Cria a entrada
        int n1, n2, soma, subtracao, multiplicao, divisao, resto;
        String prompt = "Digite um número\n>> ";
        System.out.print(prompt);
        n1 = entrada.nextInt();
        System.out.print(prompt);
        n2 = entrada.nextInt();
        soma = n1 + n2;
        subtracao = n1 - n2;
        multiplicao = n1 * n2;
        divisao = n1 / n2;
        resto = n1 % n2;
        System.out.printf("Soma: %s\nSubtração: %s\nMultiplicação: %s\nDivisão: %s\nResto: %s", soma, subtracao,
                multiplicao, divisao, resto);
    }
}
