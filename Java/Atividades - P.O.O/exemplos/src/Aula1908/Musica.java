package Aula1908;


public class Musica {
    private String titulo;
    private int duracaominutos;

    public String getTitulo() {
        return this.titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public int getDuracaominutos() {
        return this.duracaominutos;
    }
    public void setDuracaominutos(int duracaominutos) {
        this.duracaominutos = duracaominutos;
    }

    public void TocarMusica() {
        System.out.printf("Tocando agora a faixa: '%s'", this.titulo);
    }
    public Musica(String titulo, int duracaominutos) {
        this.titulo = titulo;
        this.duracaominutos = duracaominutos;
    }
}
