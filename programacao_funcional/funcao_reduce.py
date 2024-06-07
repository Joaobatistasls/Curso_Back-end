"""
variavel = reduce(funcao, colecao)
"""
# Importando a funcao reduce, não é nativa do python
from functools import reduce

# Usando a Função: reduce(funcao, colecao)
def multiplica(a, b):
    return a * b

numeros = [1, 2, 3, 4, 5]
produto = reduce(multiplica, numeros)
print(produto) # 120

