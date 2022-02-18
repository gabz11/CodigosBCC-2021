// Gabriel Farias   |   Ex. 4   |   Tabuada 1 à 10 usando laço
package Aula0508;

public class Exercicio4 {
    public static void main(String[] args)
    {
        for(int i = 0; i < 10; i++)
        {
            for(int x = 1; x < 10; x++)
            {
                System.out.printf("%dX%d=%d\n",i,x,i*x);
            }
        }
    }
}
