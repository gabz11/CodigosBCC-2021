package Aula0508;

public class Gato {
    String Nome;
    String Raca;
    String CorOlhos;
    int idade;
    boolean amigavel;
    void Arrisco() {
        System.out.printf("%s está arrisco!", this.Nome);
    }
    void Deitar(){
        System.out.printf("%s deitou...", this.Nome);
    }
    void Comer(){
        System.out.printf("%s foi comer.", this.Nome);
    }
}
