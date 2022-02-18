package Aula2309;

public class Main {
    public static void main(String[] args) {
        int[] numeros = {4,5,8,9,20,3,4,5};
        int[] div = {2,4,0,8,3,0};

        try {
            for (int i = 0; i < numeros.length; i++) {
                System.out.println(numeros[i] + "/" + div[i] + "=" + (numeros[i] / div[i]));
            }
        }
        catch (ArithmeticException e) {
            System.out.println("Não pode dividir por 0 baka");
        }
    }
}
