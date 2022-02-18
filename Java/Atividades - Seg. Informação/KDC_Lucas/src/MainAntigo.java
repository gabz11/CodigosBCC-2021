import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Random;

public class MainAntigo {

    public static int verificaNonce(int nonce) {
        return nonce * 2;
    }

    /*
        Random rand = new Random();
        Bob bob = new Bob();
        Alice alice = new Alice();
        KDC kdc = new KDC();
        int tamanho = 16;

        // Gerando as chaves para o Bob e a Alice e ligando-as ao KDC.
        bob.K_BOB = GerarKey.generateKey(rand, tamanho);
        alice.K_ALICE = GerarKey.generateKey(rand, tamanho);
        kdc.K_BOB = bob.K_BOB;
        kdc.K_AlICE = alice.K_ALICE;

        String ID = "Bob";
        String ID2 = "Alice";
        byte[] autenticaID = AES.cifra(ID, bob.K_BOB);
        byte[] requisicao = AES.cifra(ID2, bob.K_BOB);

        kdc.autentica(ID, autenticaID, requisicao, bob.K_BOB);
        byte[] chaveSessaoBob = kdc.retornaChave(kdc.K_SESSAO, bob.K_BOB);
        bob.K_SESSAO = new String(AES.decifra(chaveSessaoBob, bob.K_BOB));
        byte[] chaveSessaoAlice = kdc.retornaChave(kdc.K_SESSAO, alice.K_ALICE);
        alice.K_SESSAO = new String(AES.decifra(chaveSessaoAlice, alice.K_ALICE));

        int nonce = rand.nextInt(99999);
        alice.nonce = String.valueOf(nonce);

        byte[] nonceCifrado = AES.cifra(alice.nonce, kdc.K_SESSAO);
        bob.nonce = AES.decifra(nonceCifrado, kdc.K_SESSAO);
        int nonceCalculo = Integer.parseInt(bob.nonce);

        int novoNonce = verificaNonce(nonceCalculo);
        String novoNonceString = String.valueOf(novoNonce);
        byte[] novoNonceCifrado = AES.cifra(novoNonceString, kdc.K_SESSAO);
        String novoNonceDecifrado = AES.decifra(novoNonceCifrado, kdc.K_SESSAO);
        bob.novoNonce = novoNonceString;
        alice.novoNonce = novoNonceDecifrado;

        if (bob.novoNonce.equals(alice.novoNonce)) {
            System.out.println("Sucesso");

    } */
}
