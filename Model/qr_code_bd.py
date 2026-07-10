from Model.conexao import conectar

def qr_bd(link, caminho):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
        INSERT INTO qr_codes (link, nome_arquivo)
        VALUES (%s, %s)
    """

    cursor.execute(sql, (link, caminho))
    conexao.commit()

    cursor.close()
    conexao.close()