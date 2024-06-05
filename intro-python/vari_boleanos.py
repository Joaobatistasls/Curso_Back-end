# Variáveis Booleanas
verdadeiro = True
falso = False
print(verdadeiro)
print(False)

# Comparação Lógicas
Saldo_conta = 200
valor_saque = 400

saque = valor_saque <= Saldo_conta
print(saque) # = False

# Convertendo Variável
idade = 20 
print(bool(idade))

usuario_cadastrado = input("Digite seu usuário: ")
senha_cadastrada = input("Digite sua senha: ")

usuario = usuario_cadastrado
senha = senha_cadastrada

usuario_igual = usuario_cadastrado == usuario
senha_igual = senha_cadastrada == senha

acesso_permitido = usuario_igual & senha_igual
print(acesso_permitido)