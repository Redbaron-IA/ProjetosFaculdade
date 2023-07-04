import pymysql
from Conexao import ConectarDb

class Autores:

    def inserir_autor(self, autores):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "INSERT INTO autores (autores) VALUES (%s)"
            conexao.cursor.execute(sql, (autores,))
            conexao.conn.commit()
            print("Autor inserido com sucesso.")
        except pymysql.Error as e:
            print(f"Erro ao inserir autor: {e}")
        finally:
            conexao.desconectar()
        
    def ler_autores(self):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "SELECT * FROM autores"
            conexao.cursor.execute(sql)
            autores = conexao.cursor.fetchall()
            for autor in autores:
                print(f"ID: {autor[0]}, Nome: {autor[1]}")
        except pymysql.Error as e:
            print(f"Erro ao ler autores: {e}")
        finally:
            conexao.desconectar()

    def atualizar_autor(self, idAutor, autores):        
        conexao = ConectarDb()
        conexao.conectar()

        try:
            sql = "UPDATE autores SET autores = %s WHERE idAutor = %s"
            conexao.cursor.execute(sql, (autores, idAutor))
            conexao.conn.commit()
            print("Autor atualizado com sucesso.")

        except pymysql.Error as e:
            print(f"Erro ao atualizar autor: {e}")
    
    def excluir_autor(self, idAutor):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "DELETE FROM autores WHERE idAutor = %s"
            conexao.cursor.execute(sql, (idAutor))
            conexao.conn.commit()
            print(f"Autor excluido com sucesso.")
        
        except pymysql.Error as e:
            print(f"Erro ao tentar excluir registro: {e}")

# Teste do código com os métodos CRUD
if __name__ == "__main__":
    autores = Autores()
    autores.atualizar_autor(32, 'balanço')
    #autores.inserir_autor('josué firmindo')
    autores.ler_autores()
    