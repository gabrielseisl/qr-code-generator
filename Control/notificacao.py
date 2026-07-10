from plyer import notification

def enviar_notificacao(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        timeout=5
    )
#biblioteca feita para ter notificações no aplicativo depois de usar o qr code