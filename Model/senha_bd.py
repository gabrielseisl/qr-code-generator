from Model.conexao import conectar

def senha_bd(senha, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO senhas (senha, quantidade_caracteres)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (senha, quantidade))
    conexao.commit()

    cursor.close()
    conexao.close()