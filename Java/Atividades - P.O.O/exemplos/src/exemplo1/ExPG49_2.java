//  Gabriel Farias |    ex 2 Pg 49  |   Java: Como Aprender
package exemplo1;
import java.util.Scanner;

public class ExPG49_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int x, y, z, resultado;
        String prompt = "\nColoque o número para soma\n>> ";
        System.out.print("Programa que calcula soma de x, y ,z\n");

        System.out.print(prompt);
        x = entrada.nextInt();

        System.out.print(prompt);
        y = entrada.nextInt();

        System.out.print(prompt);
        z = entrada.nextInt();

        resultado = x + y + z;

        System.out.printf("O resultado da sua soma é:%n%d",resultado);
    }
}
