import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Random;
import java.util.Scanner;

public class Main {

    public static int verificaNonce(int nonce) {
        return nonce * 2;
    }

    public static void main(String[] args) throws IllegalBlockSizeException, NoSuchPaddingException, UnsupportedEncodingException, BadPaddingException, NoSuchAlgorithmException, InvalidKeyException {

        Scanner input = new Scanner(System.in);
        Random rand = new Random();
        KDC kdc = new KDC();
        int tamanho = 16;


        // Definindo os usuários.
        System.out.println("Qual seu nome? ");
        String id1 = input.next();
        System.out.println("Com quem você deseja falar? ");
        String id2 = input.next();

        Usuario user1 = new Usuario(id1);
        Usuario user2 = new Usuario(id2);

        System.out.printf("Os usuários são: %s e %s.\n", id1, id2);


        // Gerando as chaves para os usuários e ligando-as ao KDC.
        user1.K_USER = GerarKey.generateKey(rand, tamanho);
        user2.K_USER = GerarKey.generateKey(rand, tamanho);
        kdc.K_USER1 = user1.K_USER;
        kdc.K_USER2 = user2.K_USER;

        System.out.printf("Chave User1: %s.\n", user1.K_USER);
        System.out.printf("Chave User2: %s.\n", user2.K_USER);


        byte[] autenticaID = AES.cifra(user1.ID, user1.K_USER);     // Cifrando o ID do usuário para comprovar sua identidade.
        byte[] requisicao = AES.cifra(user2.ID, user1.K_USER);      // Cifrando o ID do destinatário para permitir o contato.


        // Enviando as informações para o KDC:
        // Parâmetro 1: Nome do usuário que deseja contatar o KDC.
        // Parâmetro 2: Seu nome criptografado em sua chave, a qual foi compartilhada com o KDC.
        // Parâmetro 3: Nome do destinatário criptografado na chave do primeiro usuário.

        System.out.println("O que está enviando pro KDC:");
        System.out.printf("ID: %s.\n", user1.ID);
        System.out.printf("ID Criptografado: %s.\n", autenticaID);
        System.out.printf("ID Destinatário Criptografado: %s.\n", requisicao);
        kdc.autentica(user1.ID, autenticaID, requisicao);


        // Retornando a chave de sessão criada com duas criptografias para o usuário.
        byte[] chaveSessaoUser1 = kdc.retornaChave(kdc.K_SESSAO, user1.K_USER);
        byte[] chaveSessaoUser2 = kdc.retornaChave(kdc.K_SESSAO, user2.K_USER);

        System.out.println("Chave de sessão:");
        System.out.printf("User1: %s.\n", chaveSessaoUser1);
        System.out.printf("User2: %s.\n", chaveSessaoUser2);


        // O usuário irá descriptografar sua chave e enviar a chave criptografada para o destinatário.
        user1.K_SESSAO = new String(AES.decifra(chaveSessaoUser1, user1.K_USER));

        System.out.printf("Chave Sessão User 1: %s.\n", user1.K_SESSAO);


        // Assim que receber a chave criptografada, o segundo usuário irá descriptografá-la com sua chave.
        user2.K_SESSAO = new String(AES.decifra(chaveSessaoUser2, user2.K_USER));

        System.out.printf("Chave Sessão User 2: %s.\n", user2.K_SESSAO);

        // Gerando um nonce aleatório e atribuindo-o ao usuário destinatário.
        int nonce = rand.nextInt(99999);
        user2.nonce = String.valueOf(nonce);

        System.out.printf("Nonce: %s\n", nonce);

        // O destinatário irá cifrar seu nonce com a chave de sessão e irá enviá-lo para o primeiro usuário.
        byte[] nonceCifrado = AES.cifra(user2.nonce, kdc.K_SESSAO);
        user1.nonce = AES.decifra(nonceCifrado, kdc.K_SESSAO);


        // Agora, ambos os usuários irão realizar o cálculo de verificação (criado previamente), gerando um novo nonce.
        int nonceCalculo = Integer.parseInt(user1.nonce);
        int novoNonce = verificaNonce(nonceCalculo);
        String novoNonceString = String.valueOf(novoNonce);
        user1.novoNonce = novoNonceString;
        user2.novoNonce = novoNonceString;


        // Em seguida, o primeiro usuário irá criptografar o novo nonce com a chave da sessão e enviá-lo para o destinatário.
        byte[] novoNonceCifrado = AES.cifra(novoNonceString, kdc.K_SESSAO);
        String novoNonceCifradoString = new String(novoNonceCifrado);
        user2.checkNonce = novoNonceCifradoString;


        // Por fim, o destinatário irá descriptografar o novo nonce e compará-lo com o seu próprio.
        String novoNonceDecifrado = AES.decifra(novoNonceCifrado, kdc.K_SESSAO);
        user2.checkNonce = novoNonceDecifrado;

        System.out.printf("Novo nonce 2: %s.\n", user2.novoNonce);
        System.out.printf("Check Nonce: %s.\n", user2.checkNonce);

        if (user2.novoNonce.equals(user2.checkNonce)) {
            System.out.println("Sucesso");
        }
    }
}
