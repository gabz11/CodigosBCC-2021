#   Gabriel Farias  |   Ex 9.6  | Intensivo de Python
class Restaurante:
    """
    Classe dos restaurantes
    """
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.servidos = 0

    def descrever(self):
        print(f'{self.nome.title()} é um restaurante do tipo {self.tipo.title()}')

    def totalservidos(self):
        print(f'Total servidos = {self.servidos}')

    def servir(self):
        self.servidos += 1


class Sorveteria(Restaurante):
    """
    Classe de sorveteria
    """
    def __init__(self, nome):
        super().__init__(nome, tipo="Sorveteria")
        self.sabores = ['vanila', 'chocolate', 'baunilha']

    def descrever(self):
        print(f'{self.nome.title()} é uma sorveteria.')

    def descreversabores(self):
        for sabor in self.sabores:
            print(f'Sabor:{sabor.title()}')


sorveteria1 = Sorveteria('gustachi')
sorveteria1.descrever()
sorveteria1.descreversabores()
