package Hash_SEG;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class LerArquivo {
    String path = "src\\Hash_SEG\\dados.txt";

    public void LerArquivo(String path_file)
    {
        path = path_file;
    }

    int lerLinhas() throws IOException
    {
        FileReader lerarquivo = new FileReader(path);
        BufferedReader br = new BufferedReader(lerarquivo);

        String umalinha;
        int numero_linhas = 0;
        while((umalinha = br.readLine()) != null)
        {
            numero_linhas++;
        }
        br.close();
        return numero_linhas;
    }

    public String[] AbrirArquivo() throws IOException
    {
        FileReader la = new FileReader(path);
        BufferedReader leitor = new BufferedReader(la);
        int num_linhas = lerLinhas();
        String[] textoArquivo = new String[num_linhas];

        for(int i = 0; i < num_linhas; i++)
        {
            textoArquivo[i] = leitor.readLine();
        }
        leitor.close();
        return textoArquivo;
    }
}
