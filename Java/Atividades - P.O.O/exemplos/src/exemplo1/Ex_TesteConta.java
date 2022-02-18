// Gabriel Farias | Pg 59 | Java: como programar
package exemplo1;
import java.util.Scanner;

public class Ex_TesteConta {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        Ex_Conta minhaConta = new Ex_Conta();
        System.out.printf("Nome inicial é %s", minhaConta.retNome());
        System.out.print("\nColoque um nome na conta\n>> ");
        String nome = entrada.next();
        minhaConta.defNome(nome);
        System.out.printf("\nO nome da conta é %s", minhaConta.retNome());
    }
}
