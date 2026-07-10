import requests
import os
import time
from tkinter import messagebox
from plyer import notification
from Control.notificacao import enviar_notificacao
from Model.imagem_bd import imagem_bd
def imagem():

    url = "https://randomfox.ca/floof/"
    #retornara uma raposa de uma api

    resposta = requests.get(url)

    
    link_imagem = resposta.json()["image"]
    #pega imagem da api

    
    imagem = requests.get(link_imagem)
    #baixa

    
    nome = f"raposa_{int(time.time())}.jpg"
    #nome do arquivo
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    caminho = os.path.join(desktop, nome)

    with open(caminho, "wb") as arquivo:
        arquivo.write(imagem.content)
    #salva imagem

    enviar_notificacao(
    "Raposa Salva",
    "Olhe sua área de trabalho"
)

   
    os.startfile(caminho)
    #abre a imagem

    imagem_bd(nome, link_imagem)


