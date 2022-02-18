// Gabriel Farias   |   exemplo 7   |   Java: Como aprender
package exemplo1;
import java.util.Scanner; // importa Scanner

public class exemplo7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int n1, n2; // int para comparação

        System.out.print("Coloque o primeiro inteiro\n>> ");
        n1 = entrada.nextInt();
        System.out.print("Coloque o 2do inteiro\n>> ");
        n2 = entrada.nextInt();

        if (n1 == n2) // n precisa de chaves para uma ação, todavia melhor usar
            System.out.printf("%d = %d", n1, n2);
        else
            System.out.printf("%d != %d", n1 , n2);
    } // Fim do MAIN
} // fim classe Exemplo 7
