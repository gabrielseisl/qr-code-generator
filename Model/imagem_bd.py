from Model.conexao import conectar

def imagem_bd(nome_arquivo, url_imagem):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO imagens (nome_arquivo, url_imagem)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (nome_arquivo, url_imagem))
    conexao.commit()

    cursor.close()
    conexao.close()