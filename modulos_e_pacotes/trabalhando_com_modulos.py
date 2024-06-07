class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f"Seu nome é {self.nome} e sua idade é {self.idade}"