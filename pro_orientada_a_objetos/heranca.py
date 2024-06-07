"""
"Classe Pai"
class NomeClasse(objeto):
    def __init__(self, params):
        pass

"Classe Filha"
class NomeClasseHeranca(NomeClasse):
    def ___init__(self, params):
        super().__init__(self, params)
        self.atributo3 = ...
        self.atributo4 = ...

    def metodo3(self, params)
        pass
    
    def metodo4(self, params)
"""
# CLASSE PAI
class Pessoa(object):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    # Chamar idade
    def chamar_pessoa(self):
        return f"O nome da pessoa é: {self.nome} e sua idade é: {self.idade}"

# CLASSE FILHA
class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int):
        # Serve para utilizamos os atributos e metodo da classe Pai
        super().__init__(nome, idade)
        self.nome = nome
        self.idade = idade

estudante = Estudante("Fulano de tal", 40)
print(estudante.chamar_pessoa())