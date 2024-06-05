# Criamos com chaves{}, seus valores não podemomser repetidos
fruta = {"banana", "maçã", "uva", "uva"}
print(fruta)
print(type(fruta))

# Operação com a - diferença em Conjunto 
frutas = {"uva", "melão", "melância", "banana"}
verduras = {"alface", "pimetão", "cebola", "pimenta"}
nao_sao_frutas = frutas - verduras
print(nao_sao_frutas)

# Metodos para conjuntos
curso = {"Exatas", "Humana", "Biológicas"}
print(curso)

# Inserir um elemento no Conjunto: set.add(val)
curso.add("Saúde")
print(curso)

# Remover um elemento do Conjuton: set.remove(val)
curso.remove("Saúde")
print(curso)

# Convertendo Lista > Conjuntos 
times_paulistas = {"São Paulo", "Corinthians", "Palmeiras", "Santos"}
lista_de_time_paulistas = list(times_paulistas)
print(lista_de_time_paulistas)