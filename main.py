from extrator_url import ExtratorURL

print("CONVERSOR DE MOEDA")

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = float(extrator_url.get_valor_parametro("quantidade"))

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_convertido = quantidade/VALOR_DOLAR
    print('R$', quantidade, 'são $', valor_convertido)
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_convertido = quantidade*VALOR_DOLAR
    print('$', quantidade, 'são R$', valor_convertido)
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
