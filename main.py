import requests
import json

urlAwesome = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
cotacoes = requests.get(urlAwesome)
cotacoes = cotacoes.json()

while True:
    print("Converta dinheiro real para qualquer outro")

    print()
    print("1 - DÓLAR")
    print("2 - EURO")
    print("3 - BITCOIN")
    print()

    tipo_de_moeda = int(input("Escolha um tipo de moeda para conversão \n"))
    print()

    moeda = 0

    if tipo_de_moeda == 1:
        cotacao = cotacoes["USDBRL"]
        moeda = float(cotacao["bid"])
    elif tipo_de_moeda == 2:
        cotacao = cotacoes["EURBRL"]
        moeda = float(cotacao["bid"])
    elif tipo_de_moeda == 3:
        cotacao = cotacoes["BTCBRL"]
        moeda = float(cotacao["bid"])

    real = float(input("Digite um dinheiro real para conversão \n"))
    print()

    total = real * moeda
    if tipo_de_moeda == 1:
        print(f"{real} real é igual a {total} dólar")
    elif tipo_de_moeda == 2:
        print(f"{real} real é igual a {total} euros")
    elif tipo_de_moeda == 3:
        print(f"{real} real é igual a {total} bitcoin")

    barras = ""
    for i in range(0, 100):
        barras += "="

    print(barras)