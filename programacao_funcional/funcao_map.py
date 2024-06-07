"""
variavel = map(funcao, colecao)
"""
# Criando Função utilizando o: map(funcao, colecao)
def dobrar(x):
    return x * 2

numeros = [1, 2, 3, 4,  5,]
dobrados = map(dobrar, numeros)
print(list(dobrados)) # [2, 4, 6, 8, 10]

# Usando a Função Lambda
numero = [1, 2, 3]
numeros_ao_cubo = map(lambda num: num ** 3, numero)
print(list(numeros_ao_cubo)) # [1, 8, 27]