# Permite exercução repetida de um bloco de codigo varias vezes
"""
for variavel_temporaria in colecao:
    <execute este codigo>
"""

# range(), permite criamos uma sequecia de numeros com o for: for variavel in range(start, stop)
for valor in range(1, 11):
    print(valor)
    print("------------------------------------")

# Usando o for para iterar um lista  e string
frutas = ["melancia", "uva", "banana", "goiaba"]
# Iterando: for variavel in variavel.list
for fruta in frutas:
    print(fruta)
    print("------------------------------------")

texto_qualquer = "Sejam Bem-Vindos"
# Iterando uma string
for caracte in texto_qualquer:
    print(caracte)
    print("------------------------------------")

# Iterando um Dicionario
pessoa = {
    "nome": "joao",
    "idade": 20,
    "cidade": "maceio"
}

for chave, valor in pessoa.items(): # keys() -> Retorna a chave == values -> Retorna o valor da chave
    print(f"a chave é: {chave} e seu valor é: {valor}")
    print("------------------------------------")

# Usando o break -> Para quebrar a exercução de um loop
for i in range(1, 10):
    if(i == 2):
        print(i)
        print("Pare a exercução")
        print("------------------------------------")
        break 
    else:
        print("Pode continuar exercutando")
        print("------------------------------------")

# Usando o continue -> Volta para exercução Inicial do codigo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)
        
        