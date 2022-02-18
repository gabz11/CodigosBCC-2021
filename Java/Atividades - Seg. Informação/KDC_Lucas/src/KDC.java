import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Random;

public class KDC {

    String K_USER1;
    String K_USER2;
    String K_SESSAO;

    public void autentica(String usuario, byte[] autentica, byte[] requisicao) throws IllegalBlockSizeException, NoSuchPaddingException, UnsupportedEncodingException, BadPaddingException, NoSuchAlgorithmException, InvalidKeyException {

        Random rand = new Random();
        int tamanho = 16;
        String textoDecifrado = AES.decifra(autentica, K_USER1);

        if (textoDecifrado.equals(usuario)) {
            this.K_SESSAO = GerarKey.generateKey(rand, tamanho);
        }
    }

    public byte[] retornaChave(String chaveSessao, String chave) throws IllegalBlockSizeException, NoSuchPaddingException, UnsupportedEncodingException, BadPaddingException, NoSuchAlgorithmException, InvalidKeyException {
        byte[] chaveSessaoEncriptada = AES.cifra(chaveSessao, chave);
        return chaveSessaoEncriptada;
    }
}
