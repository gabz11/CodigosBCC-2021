#   Gabriel Farias  |   Ex 9.7  |   Intensivo de python
class Usuario:
    """
    Criador de usuários
    """
    def __init__(self, username, nome, idade, pais):
        self.username = username
        self.nome = nome
        self.idade = idade
        self.pais = pais

    def descrever(self):
        print(f'Nome de usuário: {self.username}\nNome: {self.nome.title()},\nIdade: {self.idade}\n'
              f'Pais: {self.pais.title()}')


class Admin(Usuario):
    """
    Classe de Administradores
    """
    def __init__(self, username, nome, idade, pais):
        super().__init__(username, nome, idade, pais)
        self.permissoes = ['pode banir', 'pode criar novos grupos', 'pinto pequeno']

    def privilegios(self):
        print('Lista de privilégios:')
        for item in self.permissoes:
            print(item)


admin1 = Admin('sussyballs', 'kanye east', 30, 'EUA')
admin1.descrever()
admin1.privilegios()
