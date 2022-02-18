// Gabriel Farias   | Exercicio 6 | 0508
package Aula0508;

public class Exercicio6 {
    // Classe de casas
    String endereco;
    String cor;
    int numerocomodos;
    int habitantes;
    int valor;
    void Reformar(){
        System.out.printf("A casa do endereço '%s' sera reformada!", this.endereco);
    }
    void Valor(){
        System.out.printf("O valor do imovel é %s", this.valor);
    }
    void CortarLuz(){
        System.out.printf("A luz da residência localizada no endereço '%s' foi cortada!", this.endereco);
    }
}
