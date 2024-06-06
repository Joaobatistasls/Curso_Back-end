"""
if <booleano / comparação logica> == True:
    <execute ese codigo>
else:
    <senão execute este codigo>
"""

# Criando condições If e Else
idade = 15
maior_de_idade = 18

vc_e_maior_de_idade = idade >= maior_de_idade

if vc_e_maior_de_idade:
    print("Vc é maior de Idade!")
else:
    print("Vc não é maior de Idade!")

# Criando multiplas condições
fruta = "uva"
legurme = "cebola"

if (fruta == "uva") & (legurme == "cebola"):
    print("Vc comprou fruta e legurme")
elif (str(type(fruta)) == str) & (str(type(legurme)) == str):
    print("Vc criou uma String")
else:
    print("Erro: Valores estão errados")