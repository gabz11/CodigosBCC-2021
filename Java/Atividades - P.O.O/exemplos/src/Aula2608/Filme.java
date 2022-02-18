// Gabriel Farias
package Aula2608;

public class Filme {
    private String titulo;
    private String anoLancamento;

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAnoLancamento() {
        return anoLancamento;
    }

    public void setAnoLancamento(String anoLancamento) {
        this.anoLancamento = anoLancamento;
    }

    public Filme(String titulo, String anoLancamento) {
        this.titulo = titulo;
        this.anoLancamento = anoLancamento;
    }
}
