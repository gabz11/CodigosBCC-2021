# Gabriel Farias | Ex 9.3 pg 205 | intensivo de python
class Usuario:
    """
    Criador de usuário
    """
    def __init__(self, username, nome, sobrenome, idade, pais):
        self.u_username = username
        self.u_nome = nome
        self.u_sobrenome = sobrenome
        self.u_idade = idade
        self.u_pais = pais

    def comprimentar(self):
        print(f'Olá {self.u_sobrenome.title()},{self.u_nome.title()}!')

    def descrever(self):
        print(f'Nome de usuário: "{self.u_username}"\nNome: {self.u_nome.title()} {self.u_sobrenome.title()}',
              f'\nIdade: {self.u_idade}\nPais: {self.u_pais.title()}')


usuario1 = Usuario('gabz11', 'gabriel', 'farias', 22, 'brasil')
usuario2 = Usuario('frankalcantrapontocom', 'frank', 'alcantra', 18, 'brasil')
usuario3 = Usuario('sussusamogus', 'amogus', 'sussus', 69, 'suslandia')
usuario1.comprimentar()
usuario1.descrever()
usuario2.comprimentar()
usuario2.descrever()
usuario3.comprimentar()
usuario3.descrever()
