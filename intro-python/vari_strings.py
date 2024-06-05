nome = "João"
sobrenome =  "Batista"

# Fatiamento de String
# Indice começa do 0
email = "teste@gmail.com"

print("O indice 0 é: " + email[0])

# Outra Forma de Concatenar String
# Template String
print(f"Seu nome é: {nome} e seu sobrenome é: {sobrenome}")

# Concatenação
print(nome + sobrenome)


endereco = "Cidade Universitaria, AL, Brasil"

# Deixar a String toda MAISCULO: string.upper()
print(endereco.upper())

# Busca a String dentro da String, se ela está ou não na String: string.find("substring")
# Retorna a posição da String = 1, se não achar retorna -1
posicao = endereco.find("João")
print(posicao)

# Subtituir umas String em outra String: string.replace("antigo", "novo")
print(endereco.replace("Cidade Universitaria", "Benedito Bentes"))

# Convertendo Strign em numeros 
string_numero = "10"
print(int(string_numero))

numerico = 10
print(str(numerico))