
"""
Para fazer a requisição para esse site você utiliza a biblioteca: "requests" (pip install requests)

No nosso caso a requisição é do tipo GET: "requests.get"

Exemplos de requisições:

get -> pegar
put -> enviar
patch -> editar 
delete -> deletar

"""

import requests

def conversaocotacao(reqMoedaOrigem, reqMoedaDestino):
    # reqMoedaOrigem = "EUR"
    # reqMoedaDestino = "BRL"
    linkResquisicao = f"https://economia.awesomeapi.com.br/json/last/{reqMoedaOrigem}-{reqMoedaDestino}"
    requisicao = requests.get(linkResquisicao)
    cotacao = requisicao.json()[f"{reqMoedaOrigem}{reqMoedaDestino}"]["bid"]
    return cotacao
    #print(requisicao.json()[f"{reqMoedaOrigem}{reqMoedaDestino}"]["bid"])
#conversaocotacao()






