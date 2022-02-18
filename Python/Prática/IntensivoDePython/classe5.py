#   Gabriel Farias  |   Ex 9.5 Pág 210  | Intensivo de python
class Usuario:
    """
    Criador de usuário @docstring
    """
    def __init__(self, username, nome, sobrenome, idade, pais):
        self.u_username = username
        self.u_nome = nome
        self.u_sobrenome = sobrenome
        self.u_idade = idade
        self.u_pais = pais
        self.u_l_tentativas = 0

    def comprimentar(self):
        print(f'Olá {self.u_sobrenome.title()},{self.u_nome.title()}!')

    def descrever(self):
        print(f'Nome de usuário: "{self.u_username}"\nNome: {self.u_nome.title()} {self.u_sobrenome.title()}',
              f'\nIdade: {self.u_idade}\nPais: {self.u_pais.title()}')

    def inc_t_login(self):
        self.u_l_tentativas += 1

    def reset_t_login(self):
        self.u_l_tentativas = 0


user1 = Usuario("sussyballs", "Kanye", "East", "69", "USA")
print(user1.u_l_tentativas)
user1.inc_t_login()
print(user1.u_l_tentativas)
user1.inc_t_login()
print(user1.u_l_tentativas)
user1.reset_t_login()
print(user1.u_l_tentativas)
