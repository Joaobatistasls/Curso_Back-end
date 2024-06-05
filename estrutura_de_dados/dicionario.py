# Criando um Dicionário
brasil = {
    "Capital": "Brasilia", 
    "Idioma": "Portugues", 
    "Populacao": 210
}
# Acessamos seu valor pela chave: dict["chave"]
print(brasil["Capital"])

# Criando Dicionário Composto
cadastro = {
    "joao": {
        "nome": "Joao Batista",
        "ano_nascimento": 2004,
        "pais": {
            "pai": {
                "<nome-do-pai>": "Antonio",
                "ano_nascimento": 1979
            },
            "mae": {
                "<nome-da-mae>": "Nadielle",
                "ano_nascimento": 1980
            }
        }
    }
}
# Acessando Dicionário Composto
print(cadastro["joao"]["pais"]["mae"]["<nome-da-mae>"])

# Métodos Nativo para Dicionários

# Criando um dicionário: variavel = dict(chave = val)
pessoas = dict(
    nome = "João",
    genero = "Masculino",
    idade = 20
)
print(pessoas)

# Adicionar/Atualizar um elemento pela chave-valor: dict.update(dict)
pessoas.update({"nome": "Miguel"})
print(pessoas)

# Remover um elemento pela chave: dict.pop(key)
idade = pessoas.pop("idade")

# Convertendo Dicionário para Lista
# Acessando as chaves
listas = list(pessoas.keys())
print(listas)
#Acessando os valores
listas = list(pessoas.values())
print(listas)


