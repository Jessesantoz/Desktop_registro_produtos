import mysql.connector

# CONECTAR AO BANCO DE DADOS
def conexao(banco):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database=banco,
    )
    return conexao

# CRIAR UM REGISTRO NA TABELA
def create(produto, tipo, valor, conexao):
    cursor = conexao.cursor()
    comando = f'INSERT INTO produtos (produto, tipo, valor) VALUES ("{produto}", "{tipo}", {valor})'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()

# LER DADOS DA TABELA
def read(selecao, conexao):
    cursor = conexao.cursor()
    comando = f'SELECT {selecao} FROM produtos'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado

# ATUALIZAR DADOS NA TABELA
def updv(produto, preco, conexao):
    cursor = conexao.cursor()
    comando = f'UPDATE produtos SET valor = {preco} WHERE produto = "{produto}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()

def updt(produto, tipo, conexao):
    cursor = conexao.cursor()
    comando = f'UPDATE produtos SET tipo = "{tipo}" WHERE produto = "{produto}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()

def updp(produto, nproduto, conexao):
    cursor = conexao.cursor()
    comando = f'UPDATE produtos SET produto = "{nproduto}" WHERE produto = "{produto}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()

# DELETAR REGISTRO DA TABELA
def delect(produto, conexao):
    cursor = conexao.cursor()
    comando = f'DELETE FROM produtos WHERE produto = "{produto}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()

# TESTAR FUNÇÃO
def test(res):
    print(res)
