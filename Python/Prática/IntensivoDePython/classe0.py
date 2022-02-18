# Gabriel Farias | Classes | exemplo 1
# cria classe Dog, por padrão, é classes são capitalizadas
class Dog:
    """
    Esse é um docstring!!
    """
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sentar(self):
        print(f'{self.nome.title()} sentou!')

    def rolar(self):
        print(f'{self.nome.title()} rolou!')


meu_cachorro = Dog("Bento",6)
