# Importações
import code
import time
from unicodedata import name
from urllib import response
import requests

# Instância de Variáveis
inicio = time.time()

# Bloco de Código
# API para requisitar a última cotação das moedas
#url = "https://economia.awesomeapi.com.br/last/USD-BRL"
#url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

response = requests.get(url=url)
#print (response)
quotation = (response.json())

for i,coin in enumerate(quotation.keys()):
    date_time = quotation[coin]['create_date']
    code = quotation[coin]['code']
    name = quotation[coin]['name']
    value = quotation[coin]['bid']
    delta = quotation[coin]['pctChange']
    result = f"{name}\n{date_time} - A cotação da Moeda {code} é R${value} (variação do dia {delta}%)."
    print (result)
    print()

# Instância da Variável Fim
fim = time.time()

# Instância da Variável Tempo
tempo = round(fim - inicio,2)

# Apresentação do tempo de execução na Tela
print (f"Tempo de execução: {tempo} segundos")
