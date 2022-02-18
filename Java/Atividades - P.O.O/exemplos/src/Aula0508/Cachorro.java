// Gabriel Farias
package Aula0508;

public class Cachorro {
    private String Nome = "default";
    String Raca;
    String CorDosOlhos;
    int Idade;
    boolean Amigavel;
    void Andar()
    {
        System.out.printf("%s andou!\n", this.Nome);
    }
    void Sentar()
    {
        System.out.printf("%s sentou!\n", this.Nome);
    }
    void Deitar()
    {
        System.out.printf("%s deitou!\n", this.Nome);
    }
    void definirNome(String nomeCachorro)
    {
        this.Nome = nomeCachorro;
    }
}
