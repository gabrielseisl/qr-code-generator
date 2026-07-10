import random
from Model.senha_bd import senha_bd
def criar_senha(quantidade):

    opcoes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?"

    senha = ""

    for i in range(quantidade):
        senha += random.choice(opcoes)

    senha_bd(senha, quantidade)

    return senha

