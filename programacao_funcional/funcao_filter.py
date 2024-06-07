"""
variavel = filter(funcao, colecao)
"""
def maior_que_cinco(x):
    return x > 5

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maiores_que_cinco = filter(maior_que_cinco, numeros)
print(list(maiores_que_cinco))  # Saída: [6, 7, 8, 9, 10]

# Filter com a Função Lambda(Função Anonima)
numero = [1, 2, 3]
numeros_impares = filter(lambda num: num % 2 != 0, numero)
print(list(numeros_impares)) # [1, 3]

# De 0 ate 100
numeros_ate_cem = range(0, 101)

contagem = filter(lambda x: x % 2 != 0, numeros_ate_cem)
print(list(contagem))
"""
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35,
37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65,
67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
"""