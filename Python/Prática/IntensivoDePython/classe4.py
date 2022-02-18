#   Gabriel Farias  |   Exemplo classe  |   Intensivo de Python
class Restaurante:
    """
    Cria objetos restaurante!
    """
    def __init__(self, nome, tipo):
        self.r_nome = nome
        self.r_tipo = tipo
        self.r_p_servidas = 0

    def descrever(self):
        print(f'{self.r_nome.title()} é um restaurante do tipo {self.r_tipo.title()}')

    def servidos(self, p_servidas):
        if p_servidas > 0:
            self.r_p_servidas = p_servidas
        else:
            print('Não ha como servir pessoas nulas ou negativas')

    def totalservidos(self):
        print(f'{self.r_p_servidas} servidos!')


restaurante1 = Restaurante('sussy', 'fast food')
restaurante1.descrever()
restaurante1.totalservidos()
restaurante1.servidos(69)
restaurante1.totalservidos()
