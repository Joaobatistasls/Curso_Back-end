"""
class NomeClasse(object):
    ...

objeto = NomeClass(params, params)
objeto.atributo - Para acessamos o atributo usamos .
objeto.metodo() - metodo = funcao - Para acessamos o metodo usamos o ()
"""

class Pessoa(object):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    # Chamar idade
    def chamar_pessoa(self):
        return f"O nome da pessoa é: {self.nome} e sua idade é: {self.idade}"

pessoa1 = Pessoa("João", 20)
pessoa2 = Pessoa("maria", 52)
print(pessoa1.nome)
print(pessoa2.chamar_pessoa())