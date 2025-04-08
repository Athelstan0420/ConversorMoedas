"""

Tratando arquivos XML: estruturas segmentadas por tags. EX: 
---------------------------------------------
<?xml version="1.0" encoding="utf-8"?>

<xml>

    <BRL> Real Brasileiro </BRL>
    <USD> Dolar Americano </USD>

</xml>
----------------------------------------------

Vamos utilizar a biblioteca py: "xmltodict" -> Pega um arquivo xml e transforma em um dicionário
dentro de um dicionário. (pip install xmltodict)

API = https://docs.awesomeapi.com.br/api-de-moedas

"""

import xmltodict
#---------------------------------------------------------------------------------------------------

def nomes_moedas():
    # Abrir o arquivo moedas:
    with open("/home/adriel/Documentos/Develop/ConversorMoedas/moedas.xml", "rb") as arqMoedas:
        # Ler Arquivo xlm:
        dicionarioMoedas = xmltodict.parse(arqMoedas) # A função parse decodifica o arquivo xml e transforma ele em outra coisa.

    #print(dicionarioMoedas) # é a mesma coisa do que está abaixo:
    moedas = dicionarioMoedas["xml"]
    #print(moedas)
    return moedas
#nomes_moedas()
#---------------------------------------------------------------------------------------------------

def conversoes_disponiveis():
    # Abrir o arquivo moedasconv:
    with open("/home/adriel/Documentos/Develop/ConversorMoedas/moedasconv.xml", "rb") as moedas_convert:
        # Ler aquivo xml:
        dicionarioConv = xmltodict.parse(moedas_convert)
    #print(dicionarioConv) # é a mesma coisa do que está abaixo:
    conversoes = dicionarioConv["xml"]
#--------------------------------------------------
    dic_convert_disp = {}
    for par_convert in conversoes:
        origem, destino = par_convert.split("-")
        if origem in dic_convert_disp:
            dic_convert_disp[origem].append(destino)
        else:
            dic_convert_disp[origem] = [destino]
    return dic_convert_disp
#--------------------------------------------------
    #print(dic_convert_disp)
    
#conversoes_disponiveis()
    
#---------------------------------------------------------------------------------------------------


