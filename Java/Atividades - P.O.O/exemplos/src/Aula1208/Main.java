package Aula1208;

public class Main {
    public static void main(String[] args){
        Funcionario amogus = new Funcionario("Amon Gus", "TI", "Segurança","Vermelha",1);
        Funcionario fabricio = new Funcionario("Fabricio","Faxineiro",10000);
        Funcionario aladin = new Funcionario("John Xina","Lutador",59);
        Funcionario frankalcantra = new Funcionario("Fabricio","CEO",100000000);
        Funcionario jorge = new Funcionario("Jorge","TI","Script Kiddie", 10000);
        int somasalario = amogus.salario + fabricio.salario + aladin.salario + frankalcantra.salario + jorge.salario;
        System.out.printf("Salário dos funcionarios total: %s", somasalario);
    }
}
