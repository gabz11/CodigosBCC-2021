#   Gabriel Farias  |   Classes |   Intensivo   de  Python
class Carro:
    """
    Criador de carro
    Superclasse de CarroEletrico
    """

    def __init__(self, modelo, fabricante, ano):
        self.c_modelo = modelo
        self.c_fabricante = fabricante
        self.c_ano = ano
        self.c_kilometragem = 0

    def descrever(self):
        print(f'Modelo: "{self.c_modelo.title()}"\nFabricante:{self.c_fabricante.title()}\nAno:{self.c_ano}')

    def abastecer(self):
        print(f'{self.c_modelo.title} abasteceu o tanque!')


class Bateria:
    """
    Criador de bateria
    """

    def __init__(self, carga_bateria):
        self.b_pot_bateria = carga_bateria

    def descreverbateria(self):
        print(f'A carga da bateria é {self.b_pot_bateria} kWhz')


class CarroEletrico(Carro):
    """
    Criador de carro eletrico
    Classe-filho de Carro
    """

    def __init__(self, modelo, fabricante, ano):
        super().__init__(modelo, fabricante, ano)
        self.c_bateria = Bateria(69)


meu_carro = CarroEletrico('model s', 'tesla', 2016)
meu_carro.c_bateria.descreverbateria()
