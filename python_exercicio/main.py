"""
1. Variáveis e Tipos de Dados
Exercício: Crie variáveis para armazenar as seguintes informações: seu nome (string), sua idade (inteiro), 
sua altura (float) e se você está matriculado em um curso (booleano). Verifique o tipo de dado de cada 
uma dessas variáveis usando a função type().
"""
from functools import reduce

nome = "João"
idade = 20
altura = 1.70
curso_matriculado = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(curso_matriculado))
print("-------------------------------------")

"""
2. Operações Matemáticas
Exercício: Crie duas variáveis inteiras, a e b, com valores 10 e 3, 
respectivamente. Calcule e imprima a soma, subtração, multiplicação, divisão, divisão inteira, 
potência e o resto da divisão entre a e b.
"""
valor_a = 10
valor_b = 3

somar = valor_a + valor_a
subtracao = valor_a - valor_b
multiplicao = valor_a * valor_b
divisao = valor_a / valor_b
divisao_inteira = valor_a // valor_b
potencia = valor_a ** valor_b
resto_da_divisao = valor_a % valor_b

print(somar)
print(subtracao)
print(multiplicao)
print(divisao)
print(divisao_inteira)
print(potencia)
print(resto_da_divisao)
print("-------------------------------------")

"""
3. Strings
Exercício: Crie uma variável nome com seu nome completo. Utilize o fatiamento para extrair e imprimir seu 
primeiro nome e seu sobrenome. Em seguida, converta seu nome completo para maiúsculas e imprima o resultado.
"""
nome_compĺeto = "João Batista"
print(f"Meu nome é: {nome_compĺeto[0:4].upper()} e meu sobrenome é: {nome_compĺeto[5:12].upper()}")
print("-------------------------------------")

"""
4. Booleanos
Exercício: Crie duas variáveis booleanas, a e b, com valores True e False, respectivamente. 
Imprima o resultado das seguintes operações lógicas: a and b, a or b, not a, a == b, a != b, a > b e a < b
"""
a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print("-------------------------------------")

"""
5. Listas
Exercício: Crie uma lista chamada numeros contendo os números de 1 a 10. Em seguida, faça o seguinte:

Adicione o número 11 ao final da lista.
Remova o número 5 da lista.
Substitua o número 3 pelo número 33.
Imprima a lista resultante.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.append(11)
numeros.remove(5)
index = numeros.index(3)
numeros[index] = 33
print(numeros)
print("-------------------------------------")

"""
6. Conjuntos
Exercício: Crie dois conjuntos, A e B, com os seguintes valores:

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
Calcule e imprima a diferença entre os conjuntos A e B (elementos que estão em A mas não estão em B).
"""
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
diferenca_de_a_e_b = a - b
print(diferenca_de_a_e_b)
print("-------------------------------------")

"""
7. Dicionários
Exercício: Crie um dicionário chamado aluno com as seguintes chaves: nome, idade, curso e notas. 
As notas devem ser uma lista com três valores. Em seguida, adicione uma nova chave matricula ao dicionário e imprima o dicionário completo.
"""
aluno = {
    'nome': 'joao',
    'idade': 20,
    'notas': [7, 10, 8],
}
aluno.update({'turma': '3a'})

print(aluno)
print("-------------------------------------")

"""
8. Estruturas Condicionais
Exercício: Escreva uma função que receba um número como parâmetro e verifique 
se ele é positivo, negativo ou zero. A função deve imprimir uma mensagem apropriada para cada caso.
"""
def verificar_numero(a):
    if(a >= 1):
        return 'O número é Positivo'
    elif(a < 0):
        return 'O número é Negativo'
    else:
        return 'O número é Zero'

print(verificar_numero(2))
print("-------------------------------------")

"""
9. Estruturas de Repetição
Exercício: Escreva um loop for que percorra uma lista de números de 1 a 10 e imprima apenas os números pares.
"""
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numeros_pares in lista_numeros:
    if(numeros_pares % 2 == 0):
        print(numeros_pares)
print("-------------------------------------")

"""
10. Funções e Escopo
Exercício: Escreva uma função chamada calcula_media que receba uma lista de notas e retorne a média das notas. Dentro da função, crie uma 
variável local chamada soma para armazenar a soma das notas. Teste a função com uma lista de notas.
"""
def calcula_media(notas):
    somar = sum(notas)
    media = somar / len(notas)
    return media

lista_de_notas = [8.0, 9.0, 6.0, 7.5]
media = calcula_media(lista_de_notas)
print(media)
print("-------------------------------------")
"""
11. Funções de Alta Ordem - Map, Filter, Reduce
Exercício: Crie uma lista de números de 1 a 10. Use a função map para criar uma nova lista com o 
dobro dos valores da lista original. Em seguida, use a função filter para criar uma lista apenas com os 
números pares da lista original. Por fim, use a função reduce para calcular a 
soma de todos os números da lista original (dica: importe reduce do módulo functools).
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = map(lambda x: x * 2, lista)
print(list(nova_lista))
print("-------------------------------------")
numeros_pares = filter(lambda x: x % 2 == 0, lista)
print(list(numeros_pares))
print("-------------------------------------")
somar_numeros = reduce(lambda x, z: x + z, lista)
print(somar_numeros)
print("-------------------------------------")

"""
12. Programação Orientada a Objetos
Exercício: Crie uma classe chamada Carro com os seguintes atributos: marca, modelo e ano. A classe deve ter um método detalhes 
que imprime as informações do carro. Crie uma instância da classe e chame o método detalhes.
"""
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes_do_carro(self):
        return f'A marca do carro é: {self.marca} e seu modelo é: {self.modelo} e o ano é: {self.ano}'

carro = Carro('Fiat', 'Uno Vivace', '2012')
print(carro.detalhes_do_carro())