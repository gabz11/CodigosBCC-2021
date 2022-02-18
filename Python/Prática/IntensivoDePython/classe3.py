#   Gabriel Farias  |   Exemplo Classes   |     Intensivo de Python
# cria a classe carro
class Carro:
    """
    Eu sou um docstring!!
    """
    def __init__(self, modelo, fabricante, ano):
        self.r_modelo = modelo
        self.r_fabricante = fabricante
        self.r_ano = ano
        self.r_odometro = 0

    def descrever(self):
        print(f'\nÉ um {self.r_modelo.title()} da {self.r_fabricante.title()} do ano de {self.r_ano}')

    def verodometro(self):
        print(f'\nEsse carro tem {self.r_odometro} kilometros.')

    def aum_odometro(self, kilometragem):
        if kilometragem <= 0:
            print('\nNão se pode reduzir a kilometragem de um veiculo...')
        else:
            self.r_odometro += kilometragem


meu_carro = Carro('mustang', 'ford', 2005)
meu_carro.descrever()
meu_carro.verodometro()
meu_carro.aum_odometro(22)
meu_carro.verodometro()
meu_carro.aum_odometro(2)
meu_carro.verodometro()
meu_carro
