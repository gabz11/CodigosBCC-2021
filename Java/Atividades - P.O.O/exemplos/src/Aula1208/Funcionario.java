package Aula1208;

public class Funcionario {
    String nome;
    String cargo;
    String ramoTI;
    String corcaneta;
    int salario;
    public Funcionario(String nome, String cargo, int salario)
    {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }
    public Funcionario(String nome, String cargo, String ramoTI, int salario)
    {
        this.nome = nome;
        this.cargo = cargo;
        this.ramoTI = ramoTI;
        this.salario = salario;
    }
    public Funcionario(String nome, String cargo, String ramoTI, String corcaneta, int salario)
    {
        this.nome = nome;
        this.cargo = cargo;
        this.ramoTI = ramoTI;
        this.corcaneta = corcaneta;
        this.salario = salario;
    }
    void VerSalario() {
        System.out.printf("\nO salário de %s é %sR$", nome, salario);
    }
    void VerCorCaneta() {
        if (corcaneta == null){
            System.out.printf("\nNão tem caneta");
        }
        else {
            System.out.printf("\nA caneta é %s", corcaneta);
        }
    }
    void VerCargo() {
        System.out.printf("\nO cargo é %s", cargo);
    }
}
