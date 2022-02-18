import random


class Tabuleiro:
    """
    Classe de tabuleiros
    Contem os aspectos analogos/fisicos do jogo da velha
    Contem apenas uma lista com 9 valores que refletem
    as posições do topo esquerdo ate á ultima lateral do
    jogo da velha.
    """

    def __init__(self):
        """
        Os valores no vetor podem ser o seguinte
        0 = Espaço vázio
        1 = X (Xís)
        2 = O (Circulo)
        """
        self.tabuleiro = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def jogartabuleiro(self, ladrilho, jogador, vez):
        """
        Faz a jogada
        :param ladrilho: String/númerico(Posição no tabuleiro, para pontuação)
        :param jogador: String(X ou O, para pontuação)
        :param vez: String(Jogador ou CPU, para que no caso da CPU ele não exiba mensagem desnecessarias)
        :return: Retorna um booleano para indicar se a jogada foi um sucesso ou um erro
        """
        if ladrilho.isnumeric():
            ladrilho = int(ladrilho)
            # ladrilho é originalmente uma string e então é parseado
            if ladrilho < 9:
                if jogador == 'X':
                    jogada = 1
                    if self.tabuleiro[ladrilho] == 0:
                        self.tabuleiro[ladrilho] = jogada
                        return True
                    elif self.tabuleiro[ladrilho] != 0 and vez == 'cpu':
                        return False
                    else:
                        print("Esse ladrilho esta ocupado...")
                        return False
                elif jogador == 'O':
                    jogada = 2
                    if self.tabuleiro[ladrilho] == 0:
                        self.tabuleiro[ladrilho] = jogada
                        return True
                    elif self.tabuleiro[ladrilho] != 0 and vez == 'cpu':
                        return False
                    else:
                        print("Esse ladrilho está ocupado...")
                        return False
            else:
                print("\nPor favor escolha um ladrilho entre 0 hà 8")
        else:
            print('Comando inválido')

    def vertabuleiro(self):
        """
        Modela o tabuleiro de modo estético para o usuário
        """
        tabvisu = []
        borda = "░░░░░░░░░░░"
        for x in range(0, len(self.tabuleiro)):
            if self.tabuleiro[x] == 0:
                tabvisu.append(" ")
            elif self.tabuleiro[x] == 1:
                tabvisu.append("X")
            elif self.tabuleiro[x] == 2:
                tabvisu.append("O")
        print(f'{borda}'
              f'\n {tabvisu[0]} | {tabvisu[1]} | {tabvisu[2]} '
              f'\n-----------'
              f'\n {tabvisu[3]} | {tabvisu[4]} | {tabvisu[5]} '
              f'\n-----------'
              f'\n {tabvisu[6]} | {tabvisu[7]} | {tabvisu[8]} \n'
              f'{borda}')


class Jogo:
    """
    Classe principal do jogo
    Tem os principais metodos para inicialização
    """

    def __init__(self):
        """
        Os parametros são todos para operações booleanas para os diversos metodos do jogo.
        """
        self.jogadorTipo = " "
        # Define se joga com X ou O
        self.vez = " "
        # Define a vez
        self.cpuTipo = " "
        # Define se joga com X ou O
        self.msgInicio = " "
        # Exibe mensagem de quem começa
        self.uitipojogador = " "
        # Exibe marcação X ou O
        self.tabuleiro = Tabuleiro()
        # Instancia um tabuleiro
        self.vitoria = 0
        # Condição de vitória
        self.modoJogo = False

    def definircomeco(self):
        """
        Sorteia entre 0 e 1 e tira quem começa a partida.
        :return:
        """
        comeca = random.randint(0, 1)
        # decide quem começa
        # 0 = Jogador | 1 = CPU
        if comeca == 0:
            self.jogadorTipo = "X"
            self.vez = "jogador"
            self.cpuTipo = "O"
            self.uitipojogador = "(X)"
            self.msgInicio = "\nO Jogador começa!"
        else:
            self.jogadorTipo = "O"
            self.vez = "cpu"
            self.cpuTipo = "X"
            self.uitipojogador = "(O)"
            self.msgInicio = "\nA CPU começa!"

    def partida(self):
        """
        Metodo de chamada principal
        Declara o programa em 'Modo Jogo' e ira apenas quebrar do laço
        quando o jogo satisfazer a condição de vitória ou empatar e os turnos se esgotarem.
        :return:
        """
        self.modoJogo = True
        turno = 9
        while self.modoJogo:
            self.jogada()
            turno -= 1
            self.vervitoria(turno)
            self.mudarturno()

    def mudarturno(self):
        """
        Executa após cada turno
        :return:
        """
        if self.vez == 'jogador':
            self.vez = 'cpu'
        elif self.vez == 'cpu':
            self.vez = 'jogador'

    def menu(self):
        """
        menu principal, exibe as opções de interação.
        :return:
        """
        print('Jogo da Velha!\n Feito por Gabz Farias!')
        opcoes = '\nJ - Jogar\nI - Instrução\nS - Sair'
        while True:
            print(opcoes)
            prompt = input('\n>> ')
            if prompt == 'j' or prompt == 'J':
                self.definircomeco()
                self.partida()
            elif prompt == 'i' or prompt == 'I':
                self.instrucoes()
            elif prompt == 's' or prompt == 'S':
                print('Adeus!')
                exit()

    def instrucoes(self):
        """
        Explica as instruções do jogo
        :return:
        """
        borda = "░░░░░░░░░░░"
        print("Cada número corresponde a uma posição no tabuleiro do jogo da velha!")
        print(f'\n{borda}'
              '\n 1 | 2 | 3 '
              '\n-----------'
              '\n 4 | 5 | 6 '
              '\n-----------'
              '\n 7 | 8 | 9 \n'
              f'{borda}\n')

    def jogada(self):
        """
        Metodo para jogada, verifica se é cpu ou o jogador, tambem valida as jogadas com flags
        :return:
        """
        self.tabuleiro.vertabuleiro()
        if self.vez == "jogador":
            jogada = True
            while jogada:
                lad = self.vezjogador()
                lad = int(lad)
                lad -= 1
                lad = str(lad)
                vez_jog = self.tabuleiro.jogartabuleiro(lad, self.jogadorTipo, self.vez)
                if vez_jog == True:
                    jogada = False
                else:
                    print('Tente novamente')
        elif self.vez == "cpu":
            jogada = True
            while jogada:
                lad = random.randint(0, 8)
                lad = str(lad)
                vez_cpu = self.tabuleiro.jogartabuleiro(lad, self.cpuTipo, self.vez)
                if vez_cpu == True:
                    jogada = False
                else:
                    jogada = True

    def vezjogador(self):
        """
        Metodo para pegar a posição na qual o jogador deseja
        :return:
        """
        print(f'Sua marcação: {self.jogadorTipo}')
        prompt = input('Qual ladrilho você quer jogar?\n>> ')
        return prompt

    def vervitoria(self, turno):
        """
        Verifica o jogo para ver as ocorrências de vitória
        :param turno:
        :return:
        """
        v = self.tabuleiro.tabuleiro
        linhaX = [1, 1, 1]
        linhaO = [2, 2, 2]
        # horizontais x
        condX1 = v[0:3] == linhaX
        condX2 = v[3:6] == linhaX
        condX3 = v[6:9] == linhaX
        # diagonais x
        condX4 = v[0] == 1 and v[4] == 1 and v[8] == 1
        condX5 = v[2] == 1 and v[4] == 1 and v[6] == 1
        # verticais x
        condX6 = v[0] == 1 and v[3] == 1 and v[6] == 1
        condX7 = v[2] == 1 and v[5] == 1 and v[8] == 1

        # horizontais x
        condO1 = v[0:3] == linhaO
        condO2 = v[3:6] == linhaO
        condO3 = v[6:9] == linhaO
        # diagonais x
        condO4 = v[0] == 2 and v[4] == 2 and v[8] == 2
        condO5 = v[2] == 2 and v[4] == 2 and v[6] == 2
        # verticais x
        condO6 = v[0] == 2 and v[3] == 2 and v[6] == 2
        condO7 = v[2] == 2 and v[5] == 2 and v[8] == 2

        if condX1 or condX2 or condX3 or condX4 or condX5 or condX6 or condX7:
            self.tabuleiro.vertabuleiro()
            print('X ganhou')
            self.tabuleiro.tabuleiro = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.modoJogo = False
        elif condO1 or condO2 or condO3 or condO4 or condO5 or condO6 or condO7:
            self.tabuleiro.vertabuleiro()
            print('O ganhou')
            self.tabuleiro.tabuleiro = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.modoJogo = False
        elif turno == 0:
            self.tabuleiro.vertabuleiro()
            print('Ninguem ganhou!')
            self.tabuleiro.tabuleiro = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.modoJogo = False
        else:
            pass


jg1 = Jogo()
jg1.menu()
