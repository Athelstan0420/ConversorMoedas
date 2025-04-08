import customtkinter as CTKI
from pegarMoedas import *
from pegarCotacao import *

CTKI.set_appearance_mode("dark") # aparencia da janela.

janela = CTKI.CTk()
janela.title("Conversor de Moedas")

dicconvdisp = conversoes_disponiveis() #chamando a função de pegarmoedas;

#-----------------------------------------------------------------------------------------
titulo = CTKI.CTkLabel(janela,text="Conversor de Moedas", font=("",50))

def carregarMoedasDestino(moedaSelecionada):
    listaDestino = dicconvdisp[moedaSelecionada]
    menu_moedas_destino.configure(values=listaDestino)
    menu_moedas_destino.set(listaDestino[0]) 

de = CTKI.CTkLabel(janela, text="Converter:", font=("",30))
menu_moedas_origem = CTKI.CTkOptionMenu(janela, values=list(dicconvdisp.keys()), command=carregarMoedasDestino) #Cria um menu de opções;

para = CTKI.CTkLabel(janela, text="Para:", font=("",30))
menu_moedas_destino = CTKI.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"]) #Cria um menu de opções;
#-----------------------------------------------------------------------------------------

#Botão converter:

def pegarCotacaoMoeda():
    coinorigem = menu_moedas_origem.get()
    coindestino = menu_moedas_destino.get()
    if coinorigem and coindestino:
        cot = conversaocotacao(coinorigem, coindestino)
        textcotacao.configure(text=f"{coinorigem} = {cot} {coindestino}")
botao_convert = CTKI.CTkButton(janela, text="Converter", command=pegarCotacaoMoeda)
textcotacao = CTKI.CTkLabel(janela, text="")

#-----------------------------------------------------------------------------------------

#lista de exibição de moedas - Frame = Vários textos em uma janela. - subjanelas dentro da janela;
tituloNomesMoedas = CTKI.CTkLabel(janela, text="Nomes das Moedas", font=("",30))
lista_moedas = CTKI.CTkScrollableFrame(janela)

moedas_disponiveis = nomes_moedas()

for cod_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[cod_moeda]
    name_moeda = CTKI.CTkLabel(lista_moedas, text=f"{cod_moeda}: {nome_moeda}")
    name_moeda.pack()

#-----------------------------------------------------------------------------------------

#Mostar na tela principal:
titulo.pack(padx=10, pady=10)
de.pack(padx=10, pady=10)
menu_moedas_origem.pack(padx=10)
para.pack(padx=10, pady=10)
menu_moedas_destino.pack(padx=10)
botao_convert.pack(padx=10, pady=20)
textcotacao.pack(padx=10, pady=10)
tituloNomesMoedas.pack(padx=10)
lista_moedas.pack(padx=10, pady=10)

#-----------------------------------------------------------------------------------------

janela.mainloop()

