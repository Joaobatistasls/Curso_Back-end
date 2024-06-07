# Usando o requests do pypi
# Usamos o requests para fazer requisições com python
import requests as req # Apelidando o requests

response = req.get('https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx')
# Para verificar se deu certo verficamos o 
print(response.status_code)

# Pegando a informação ficar no formato de texto que é o atributo
# É uma string mesmo parecendo um dicionario
print(response.text)