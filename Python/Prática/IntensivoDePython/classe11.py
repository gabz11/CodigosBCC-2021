#   Gabriel Farias  |   Ex 9.9  |   Intensivo de  Python
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

    def obter_alcance(self):
        if self.b_pot_bateria < 70:
            alcance = "fora do padrão"
        elif self.b_pot_bateria < 85:
            alcance = 240
        else:
            alcance = 270
        mensagem = "Esse carro pode ir "+str(alcance)+" km em uma carga de "+str(self.b_pot_bateria)+" kWh"
        print(mensagem)

class CarroEletrico(Carro):
    """
    Criador de carro eletrico
    Classe-filho de Carro
    """

    def __init__(self, modelo, fabricante, ano):
        super().__init__(modelo, fabricante, ano)
        self.c_bateria = Bateria(80)

meu_carro = CarroEletrico('carro gay eletrico','tesla foi um viado', 1900)
meu_carro.c_bateria.obter_alcance()