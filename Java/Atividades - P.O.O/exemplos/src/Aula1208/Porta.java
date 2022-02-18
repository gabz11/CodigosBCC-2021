package Aula1208;

public class Porta {
    boolean aberta = false;
    String cor;
    void Abrir(){
        if(this.aberta == false){
            this.aberta = true;
            System.out.printf("A porta foi aberta\n");
        }
        else{
            System.out.printf("A porta já aberta...\n");
        }
    }
    void Fechar(){
        if(this.aberta == true){
            this.aberta = false;
            System.out.printf("A porta foi fechada.\n");
        }
        else {
            System.out.printf("A porta já está fechada...\n");
        }
    }
    void Verificar(){
        if(this.aberta == true){
            System.out.printf("A porta está aberta.");
        }
        else{
            System.out.printf("A porta está fechada.");
        }
    }
    void pintarPorta(String corPorta){
        this.cor = corPorta;
    }
}
