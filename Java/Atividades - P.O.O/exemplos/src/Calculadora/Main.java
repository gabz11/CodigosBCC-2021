package Calculadora;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String prompt, n1, n2;
        Operacoes op = new Operacoes();


        System.out.print("CALCULADORA\n1. Somar\n2. Subtrair\n3. Multiplicar\n4. Resto\n5. Dividir\nS. Sair");
        while(true) {
            System.out.print("\nEscolha uma opção\n>> ");
            prompt = entrada.next();
            if(prompt.equals("1")) {
                System.out.print("\n1° número à ser somado\n>> ");
                try {
                    op.setN1(entrada.nextInt());
                }
                catch (InputMismatchException e) {
                    System.out.print("Valor Inválido");
                }
                entrada.nextLine();
                System.out.print("\n2° número à ser somado\n>>");
                op.setN2(entrada.nextInt());
                System.out.printf("\nResultado da soma de %s + %s é %s", op.getN1(), op.getN2(), op.Somar());
            }
            else if(prompt.equals("s")|| prompt.equals("S")) {
                System.exit(0);
            }
        }
    }
}
