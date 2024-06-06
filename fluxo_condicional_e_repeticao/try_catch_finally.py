# Criando try e except
# Estrutura para tratar exceções
preco = 143.20
pessoas = 0

# Para dizer que tem um erro no cógido
try:
    valor_por_pessoa = preco / pessoas
    print(valor_por_pessoa)
except Exception as erro: # se não sabe o tipo do erro coloca apenas o: Exception
    print(erro)
    print("Criando error generico")


# Usando o finally > para exercuta o codigo com erro ou não
nome = "João Batista"
idade = 20

try: 
    apresentacao = "Fala pessoal" + idade + "nome" + nome
    print(apresentacao)
except TypeError:
    idade = str(idade)
finally:
    print("Segunda chamce")
    apresentacao = "Fala pessoal" + idade + "nome" + nome
    print(apresentacao)