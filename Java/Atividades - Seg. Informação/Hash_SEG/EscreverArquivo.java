package Hash_SEG;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.IOException;

public class EscreverArquivo {
    String path;
    boolean adc_arq;

    public EscreverArquivo()
    {
        path = "src\\Hash_SEG\\dados.txt";
        adc_arq = true; // se for falso sobreescreve arquivo
    }
    void escreverLinha(String texto) throws IOException
    {
        FileWriter escrever = new FileWriter(path,adc_arq);
        PrintWriter escrever_linha = new PrintWriter(escrever);
        escrever_linha.printf("%s" + "%n",texto); // da pra colocar salt aq, %n pula linha
        escrever_linha.close();
    }
}
