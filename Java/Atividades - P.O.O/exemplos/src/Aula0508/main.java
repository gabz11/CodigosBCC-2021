package Aula0508;

public class main {
    public static void main(String[] args)
    {
        Cachorro cachorro = new Cachorro();
        cachorro.Andar();
        cachorro.definirNome("Bento");
        cachorro.Andar();
        cachorro.Sentar();
        cachorro.Deitar();
        Exercicio6 casa = new Exercicio6();
        casa.CortarLuz();
    }
}
