# Gabriel Farias | Ex 9.1 Página 205 | Intensivo de python
class Restaurante:
    """
    Classe criadora de restaurantes
    """
    def __init__(self, r_nome, r_tipo):
        self.r_nome = r_nome
        self.r_tipo = r_tipo
        # atributos de um restaurante


    def descrever(self):
        # descreve o restaurante
        print(f'{self.r_nome.title()} é um restaurante do tipo "{self.r_tipo.title()}"')


    def abrir(self):
        # abre o restaurante
        print(f'{self.r_nome.title()} esta aberto!')


# Ex 9.2 | 3 instâncias
restaurante1 = Restaurante("capressi", "italiano")
restaurante2 = Restaurante("barry bbq", "hamburgueria/americano")
restaurante3 = Restaurante("sem liçença", "brasileiro")
restaurante1.descrever()
restaurante1.abrir()
restaurante2.descrever()
restaurante2.abrir()
restaurante3.descrever()
restaurante3.abrir()
