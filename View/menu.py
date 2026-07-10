import tkinter as tk
from tkinter import messagebox
import ctypes

# Importa as funções do projeto
from Control.gerador_qr import criar_qrcode
from Control.gerador_barras import criar_codigo_de_barras
from Control.gerador_de_senha import criar_senha
from Control.imagem import imagem

try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("QR code")
except Exception:
    pass



# ===================================
# BOTÕES
# ===================================

def abrir_qrcode():
    criar_qrcode()


def abrir_barcode():
    criar_codigo_de_barras()


def abrir_imagem():
    imagem()


def gerar():
    try:
        quantidade = int(entrada.get())

        if quantidade <= 0:
            messagebox.showerror("Erro", "Digite um número maior que zero!")
            return

        senha = criar_senha(quantidade)

        resultado.config(text=f"Sua senha: {senha}")

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números!")


# ===================================
# JANELA
# ===================================

janela = tk.Tk()

janela.iconbitmap("Img/icon.ico")

janela.title("QR Code Generator")

janela.configure(bg="#1C1C1C")

# Centralizar janela
largura = 500
altura = 650

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

janela.geometry(f"{largura}x{altura}+{x}+{y}")

janela.resizable(False, False)


# ===================================
# TÍTULO
# ===================================

titulo = tk.Label(
    janela,
    text="QR Code Generator",
    font=("Segoe UI", 24, "bold"),
    bg="#1C1C1C",
    fg="#00BFFF"
)

titulo.pack(pady=(25, 5))

subtitulo = tk.Label(
    janela,
    text="Made by Gabriel Seisl",
    font=("Segoe UI", 10, "italic"),
    bg="#1C1C1C",
    fg="#A0A0A0"
)

subtitulo.pack(pady=(0, 25))


# ===================================
# BOTÃO QR CODE
# ===================================

botao_qr = tk.Button(
    janela,
    text="Gerar QR Code",
    width=28,
    height=2,
    font=("Segoe UI", 10, "bold"),
    bg="#000000",
    fg="white",
    activebackground="#000000",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=abrir_qrcode
)

botao_qr.pack(pady=8)


# ===================================
# BOTÃO CÓDIGO DE BARRAS
# ===================================

botao_barra = tk.Button(
    janela,
    text="Código de Barras",
    width=28,
    height=2,
    font=("Segoe UI", 10, "bold"),
    bg="#000000",
    fg="white",
    activebackground="#000000",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=abrir_barcode
)

botao_barra.pack(pady=8)


# ===================================
# BOTÃO RAPOSA
# ===================================

botao_imagem = tk.Button(
    janela,
    text="Raposa Aleatória",
    width=28,
    height=2,
    font=("Segoe UI", 10, "bold"),
    bg="#000000",
    fg="white",
    activebackground="#000000",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=abrir_imagem
)

botao_imagem.pack(pady=8)


# ===================================
# SENHAS
# ===================================

texto = tk.Label(
    janela,
    text="Quantidade de caracteres",
    font=("Segoe UI", 11),
    bg="#1C1C1C",
    fg="white"
)

texto.pack(pady=(25, 8))

entrada = tk.Entry(
    janela,
    width=18,
    font=("Segoe UI", 12),
    justify="center",
    bg="#2D2D2D",
    fg="white",
    insertbackground="white",
    relief="flat"
)

entrada.pack()

botao_senha = tk.Button(
    janela,
    text="Gerar Senha",
    width=28,
    height=2,
    font=("Segoe UI", 10, "bold"),
    bg="#000000",
    fg="white",
    activebackground="#000000",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=gerar
)

botao_senha.pack(pady=15)

resultado = tk.Label(
    janela,
    text="",
    font=("Consolas", 12, "bold"),
    bg="#1C1C1C",
    fg="#7CFC00"
)

resultado.pack(pady=10)


# ===================================
# BOTÃO SAIR
# ===================================

sair = tk.Button(
    janela,
    text="Sair",
    width=28,
    height=2,
    font=("Segoe UI", 10, "bold"),
    bg="#000000",
    fg="white",
    activebackground="#000000",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=janela.destroy
)

sair.pack(pady=25)

janela.mainloop()