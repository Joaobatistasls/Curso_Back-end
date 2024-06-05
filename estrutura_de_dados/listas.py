lista_nomes = ["João", "Maria", "Miguel", "Neto", 20, 52, 5, 4] 
# Criamos uma listas com Colchetes, seu valores são separados por virgula,
print(type(lista_nomes))

# Concatenando Lista
lista_vogal = ["a", "e", "i", "o", "u"]
lista_consoante = ["a", "b", "c", "d", "e"]
letras = lista_vogal + lista_consoante
print(type(letras))

# Alterando lista pelo indice
numeros = [1, 2, 3, 4, 5]
numeros[4] = 6
print(numeros)

# Inserir um elemento sem subtituir: list.insert(index, val)
juros = [0.1, 0.2, 0.3, 0.4, 0.5]
juros.insert(5, 0.6)
print(juros)

# Inserir um elemento no final da lista: list.append(val)
juros.append(0.7)
print(juros)

# Remover um elemento da lista, pelo seu valor: list.remove(val)
juros.remove(0.7)
print(juros)

# Remover um elemento da lista, pelo seu indice: list.pop(index)
juros.pop(5)

# Covertendo String > List
email = "joao@gmail.com"
caracteres_email = list(email)
print(caracteres_email)