from Model.conexao import conectar

def barras_bd(codigo, caminho):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO codigos_barras (codigo, caminho) VALUES (%s, %s) """

    cursor.execute(sql, (codigo, caminho))
    conexao.commit()

    cursor.close()
    conexao.close()