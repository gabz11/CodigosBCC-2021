//  Gabriel Farias | Ex de revisão Pg 49 |  java: como programar
package exemplo1; // pacote
import java.util.Scanner; // importa scanner

public class exPG49 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int c, thisIsAVariable, q76354, number;
        String prompt = "Coloque um inteiro\n>>";
        System.out.print(prompt);
        c = entrada.nextInt();
        thisIsAVariable = c;
        q76354 = thisIsAVariable;
        number = q76354;
        if(number == 7)
            System.out.print("Seu número é igual à 7");
        else
            System.out.print("Seu número NÃo é igual à 7");
    } // fim do metodo Main
} // fim da classe "exPG49"
