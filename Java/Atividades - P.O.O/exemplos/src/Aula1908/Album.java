package Aula1908;
import java.util.ArrayList;

public class Album {
    private String genero;
    private int ano;
    private String nome;
    private Pessoa artista;
    private ArrayList<Musica> musicas;

    public Album(String genero, int ano, String nome, Pessoa artista) {
        this.genero = genero;
        this.ano = ano;
        this.nome = nome;
        this.artista = artista;
        this.musicas = new ArrayList<Musica>();
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Pessoa getArtista() {
        return artista;
    }

    public void setArtista(Pessoa artista) {
        this.artista = artista;
    }

    public ArrayList<Musica> getMusicas() {
        return musicas;
    }

    public void setMusicas(ArrayList<Musica> musicas) {
        this.musicas = musicas;
    }

    public void mostraTodosOsDados() {
        System.out.printf("Nome album:%s\nGenero:%s\nAno:%s\nArtista:%s\nMusica:%s", this.nome, this.genero, this.ano, this.artista.getNome(), this.musicas);
    }
    public Album(String nome, String genero, int ano, Pessoa artista, ArrayList<Musica> musicas) {
        this.nome = nome;
        this.genero = genero;
        this.ano = ano;
        this.artista = artista;
        this.musicas = musicas;
    }
}
