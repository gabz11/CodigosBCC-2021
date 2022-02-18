#   Gabriel Farias  |   Exemplo Classes   |     Intensivo de Python
# cria a classe carro
class Carro:
    """
    Eu sou um docstring!!
    """
    def __init__(self, modelo, fabricante, ano):
        self.c_modelo = modelo
        self.c_fabricante = fabricante
        self.c_ano = ano
        self.c_odometro = 0

    def descrever(self):
        print(f'\nÉ um {self.c_modelo.title()} da {self.c_fabricante.title()} do ano de {self.c_ano}')

    def verodometro(self):
        print(f'\nEsse carro tem {self.c_odometro} kilometros.')

    def aum_odometro(self, kilometragem):
        if kilometragem <= 0:
            print('\nNão se pode reduzir a kilometragem de um veiculo...')
        else:
            self.c_odometro += kilometragem

    def abastecer(self):
        print('Abastecendo tanque de gasolina!')


class CarroEletrico(Carro):
    """
    Classe-filha que herda da classe "Carro"
    """
    def __init__(self, modelo, fabricante, ano):
        super().__init__(modelo, fabricante, ano)
        self.c_bateria = 0

    def descreverbateria(self):
        print(f'A batéria do {self.c_modelo} tem {self.c_bateria} kWh de potência!')

    def abastecer(self):
        print('Carros elétricos não tem tanque de gasolina....')


meu_carro = CarroEletrico("fusca", "suswalkgen", 1984)
meu_carro.descrever()
meu_carro.verodometro()
meu_carro.abastecer()
meu_carro2 = Carro("mustang","ford",1992)
meu_carro2.descrever()
meu_carro2.verodometro()
meu_carro2.abastecer()