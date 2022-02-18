// Gabriel Farias | Exemplo 3 | Adição
package exemplo1; // nome do pacote
import java.util.Scanner; // importa classe scanner

public class exemplo3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // Cria um scanner, este serve para pode obter dados de entrada

        int numero1; // declara uma variavel do tipo int com o nome numero1
        int numero2; // declara uma variavel do tipo int com o nome numero2
        String mensagem = "Seu número aqui\n>>"; // declara uma variavel do tipo String com uma mensagem
        System.out.print(mensagem); // Mensagem do prompt
        numero1 = input.nextInt(); // Prompt
        System.out.print(mensagem); // Mensagem do prompt
        numero2 = input.nextInt(); // Prompt
        int soma = numero1 + numero2; // declara uma variavel do tipo int soma q soma os valores de entrada
        System.out.printf("Sua soma é: \t%d", soma); // print format exibe uma mensagem mas o valor da soma
    }// Final do metodo MAIN
} // Final da classe exemplo 3
