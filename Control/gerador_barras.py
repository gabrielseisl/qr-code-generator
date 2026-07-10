import os
import time
from barcode import EAN13
# biblioteca que faz o padrão de código de barras EAN13 (13 dígitos, usado em produtos)

from barcode.writer import ImageWriter
# biblioteca que permite salvar o código de barras como imagem (PNG, JPG etc)

from Control.notificacao import enviar_notificacao
from Model.barras_bd import barras_bd


def criar_codigo_de_barras():
    while True:
        codigo_de_barras = input("Digite 12 ou 13 números (ou 'sair'): ")

        if codigo_de_barras.lower() == "sair":
            print("dando o fora")
            break

        if not codigo_de_barras.isdigit():
            print("por favor digite um número")
            # feito para validar os numeros do usuario
            continue

        if len(codigo_de_barras) not in [12, 13]:
            print("precisa ter 12 ou 13 números")
            # len() contara os caracteres que foram digitados.
            continue

        print(codigo_de_barras)

        barcode = EAN13(codigo_de_barras[:12], writer=ImageWriter())

        nome = f"codigo_de_barras_{int(time.time())}"
        # cria um nome único para o arquivo usando o horário atual em segundos,
        # evitando que um código de barras sobrescreva outro.

        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        salvamento = os.path.join(desktop, nome)
       

        enviar_notificacao(
        "Código de barras salvo",
        "Olhe sua área de trabalho"
        )

        print("código de barras salvo na área de trabalho")

        barcode.save(salvamento)

        caminho = salvamento + ".png"
        barras_bd(codigo_de_barras, caminho)