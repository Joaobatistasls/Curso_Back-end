"""
1. Dados de interação de usuários com propagandas
online
Na lista propaganda_online abaixo, estão presente os dados de usuários que acessaram
um determinado site e se o mesmo clicou em uma propaganda
"""

propaganda_online = [
    {'tempo_gasto_site': 68.95, 'idade': 35, 'renda_area': 61833.90,
    'tempo_gasto_internet': 256.09, 'cidade': 'Wrightburgh',
    'pais': 'Tunisia', 'clicou_no_ad': 0
    },
    {'tempo_gasto_site': 80.23, 'idade': 31, 'renda_area': 68441.85,
    'tempo_gasto_internet': 193.77, 'cidade': 'West Jodi',
    'pais': 'Nauru', 'clicou_no_ad': 0
    },
    {'tempo_gasto_site': 69.47, 'idade': 26, 'renda_area': 59785.94,
    'tempo_gasto_internet': 236.50, 'cidade': 'Davidton',
    'pais': 'San Marino', 'clicou_no_ad': 0
    },
    {'tempo_gasto_site': 68.37, 'idade': 35, 'renda_area': 73889.99,
    'tempo_gasto_internet': 225.58, 'cidade': 'South Manuel',
    'pais': 'Iceland', 'clicou_no_ad': 0
    },
    {'tempo_gasto_site': 88.91, 'idade': 33, 'renda_area': 53852.85,
    'tempo_gasto_internet': 208.36, 'cidade': 'Brandonstad',
    'pais': 'Myanmar', 'clicou_no_ad': 0
    },
    {'tempo_gasto_site': None, 'idade': 48, 'renda_area': 24593.33,
    'tempo_gasto_internet': 131.76, 'cidade': 'Port Jefferybury',
    'pais': 'Australia', 'clicou_no_ad': 1
    },
    {'tempo_gasto_site': 74.53, 'idade': 30, 'renda_area': 68862.00,
    'tempo_gasto_internet': 221.51, 'cidade': 'West Colin',
    'pais': 'Grenada'},
    {'tempo_gasto_site': 69.88, 'idade': 20, 'renda_area': 55642.32,
    'tempo_gasto_internet': 183.82, 'cidade': 'Ramirezton',
    'pais': 'Ghana', 'clicou_no_ad': 0
    }
]
"""
Para iterar pelos elementos da lista, use o código abaixo.
"""
for dado_de_usuario in propaganda_online:
    print(dado_de_usuario)
    print("---------------------------------------")

"""
1.1. Crie uma lista chamada paises com o pais dos usuários com mais de 30 anos
"""
paises = []
for dado_de_usuario in propaganda_online:
    if dado_de_usuario["idade"] >= 30:
        paises.append(dado_de_usuario["idade"])

print(f"Os usuários com mais de 30 anos são: {paises}")
print("---------------------------------------")

"""
1.2. Crie uma lista chamada leads com a renda dos usuários que clicaram na propaganda.
"""
leads = []
for dado_de_usuario in propaganda_online:
    if dado_de_usuario["renda_area"]:
        leads.append(dado_de_usuario["renda_area"])
print(f"As rendas são: {leads}")
print("---------------------------------------")

"""
1.3. Crie uma lista chamada cidades com a cidade dos usuários que passaram mais de 70
segundos no site
"""
cidades = []
for dado_de_usuario in propaganda_online:
    if dado_de_usuario["tempo_gasto_site"] is not None and dado_de_usuario["tempo_gasto_site"] >= 7:
        cidades.append(dado_de_usuario["cidade"]) 
print(cidades)