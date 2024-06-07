"""
variavel = lambda params: expressão
"""
# Criando Função Lambda para extrair o email
extrair_provedor_email = lambda email: email.split(sep="@")[-1]
email = "joao@gmail.com"
print(email)

provedor_email = extrair_provedor_email(email) # Extraindo o email
print(provedor_email)

somar = lambda a, b: a + b # Criando função Lambda
resultado = somar(10, 5)
print(resultado)

# Colocando estrutura condicional
numero_e_par = lambda numero: True if numero % 2 == 0 else False
numeros = range(0, 10)
for numero in numeros:
    if numero_e_par(numero) == True:
        print(f"O numero {numero} é par!")

# Função Alta Ordem
def multiplicador(multiplicador):
    def multiplicar(x):
        return x * multiplicador
    return multiplicar

dobro = multiplicador(2)
print(dobro(5))