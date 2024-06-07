"""
def <nome>(paramentro, paramentro):
    <bloco de codigo>
    return <valor do retorno>
"""
# Criando uma função
def somar(a, b) -> int:
    return a + b

print(somar(10, 5))
print("--------------------------")

# Texto em Maiusculo - str é pra Tipificando o retorno da nossa função
def maiusculo(texto) -> str:
    texto_maiusculo = texto.upper()
    return texto_maiusculo

print(maiusculo("seja bem-vindos"))
print("--------------------------")

# Função com Parametro - str é pra Tipificando o retorno da nossa função
def pessoa(nome: str, sobrenome: str) -> str:
    nome_completo = nome + " " + sobrenome
    return nome_completo

print(pessoa("João", "Batista"))
print("--------------------------")

# Função sem Parametro
def nome() -> None:
    return "Fulano"

nome_qualquer = nome()
print(nome_qualquer)