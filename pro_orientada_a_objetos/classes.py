"""
class NomeClasse(objeto):
    def __init__(self, params):
        self.atributo1 = ...
        self.atributo2 = ...

    def metodo1(self, params):
        ....
    def metodo2(self, params):
        ...
"""

class Pessoa(object):
    # Criando Atributos da classe - Funciona como variavel
    def __init__(self, nome: str, idade: int, documento: str = None): # Devemos sempre criar a funçaõ init quando criamos uma classe
        self.nome = nome
        self.idade = idade
        self.documento = documento

    # Crriando os metodos - Funciona como ações da classe
    def dizer_nome(self):
        return f"Meu nome é {self.nome}"
    
    # Para quando demos um print na tela mesmo sem chamar um metodo vai sair esse metodo str
    # São chamado de metodos magicos 
    def __str__(self) -> str:
        return f"Qual o seu nome: {self.nome} e sua idade: {self.idade} "
    
pessoa = Pessoa("Joao", 20, "123")
print(pessoa.dizer_nome())