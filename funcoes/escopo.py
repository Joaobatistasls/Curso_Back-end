# Escopo global
mensagem_global = "Olá, Mundo!"

def exibir_mensagem():
    print(mensagem_global)

exibir_mensagem()

# Escopo Local
def minha_funcao():
    # Variável local
    mensagem_local = "Olá, Mundo!"
    print(mensagem_local)

minha_funcao() 