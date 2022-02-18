// Gabriel Farias | Teste de instância | Calculadora
package MeusProgramas.Calculadora;
import java.util.Scanner;

public class exSoma {
    public static void main(String[] args) {
        Soma minhaSoma = new Soma();
        Scanner entrada = new Scanner(System.in);
        int numero1, numero2;
        String prompt = "Coloque seu termo para soma aqui\n>> ";
        System.out.print(prompt);
        numero1 = entrada.nextInt();
        System.out.print(prompt);
        numero2 = entrada.nextInt();
        minhaSoma.Somar(numero1,numero2);
        System.out.printf("Resultado da soma é: %d",minhaSoma.obterSoma());
    }
}
