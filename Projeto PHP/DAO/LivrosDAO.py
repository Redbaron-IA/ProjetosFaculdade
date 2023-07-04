import pymysql
from Conexao import ConectarDb

class Livros:

    def inserir_livro(self, titulo, editora, edicao, fichaCatalogo, nomeAutor):
        conexao = ConectarDb()
        conexao.conectar()

        try:          
            sql_id_autor = "SELECT idAutor FROM autores WHERE autores = %s"
            conexao.cursor.execute(sql_id_autor, (nomeAutor,))
            resultado = conexao.cursor.fetchone()
            idAutor = resultado[0] if resultado else None

            sql_livro = "INSERT INTO livros (titulo, editora, edicao, fichaCatalogo, idAutor) VALUES (%s, %s, %s, %s, %s)"
            conexao.cursor.execute(sql_livro, (titulo, editora, edicao, fichaCatalogo, idAutor))
            conexao.conn.commit()
            
            print("Livro inserido com sucesso.")
        except pymysql.Error as e:
            print(f"Erro ao inserir livro: {e}")
        finally:
            conexao.desconectar()
        
    def ler_livro(self):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "SELECT * FROM livros"
            conexao.cursor.execute(sql)
            livros = conexao.cursor.fetchall()
            for livro in livros:
                print(f"ID: {livro[0]}, Titulo: {livro[1]}, Editora: {livro[2]}, Edição: {livro[3]}, Ficha Catalografica: {livro[4]}, Autor: {livro[5]}")
        except pymysql.Error as e:
            print(f"Erro ao ler livros: {e}")
        finally:
            conexao.desconectar()

    def atualizar_livro(self, registro, titulo, editora, edicao, fichaCatalogo, idAutor):        
        conexao = ConectarDb()
        conexao.conectar()

        try:
            sql = "UPDATE livros SET titulo = %s, editora = %s, edicao = %s, fichaCatalogo = %s WHERE registro = %s"
            conexao.cursor.execute(sql, (titulo, editora, edicao, fichaCatalogo, registro))
            conexao.conn.commit()
            print("Livro atualizado com sucesso.")

        except pymysql.Error as e:
            print(f"Erro ao atualizar livro: {e}")
    
    def excluir_livro(self, registro):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "DELETE FROM livros WHERE registro = %s"
            conexao.cursor.execute(sql, (registro))
            conexao.conn.commit()
            print(f"livros excluido com sucesso.")
        
        except pymysql.Error as e:
            print(f"Erro ao tentar excluir registro: {e}")

# Teste do código com os métodos CRUD
if __name__ == "__main__":
    livros = Livros()
    
    livros.atualizar_livro(2, 'Memorias Postumas', 'Artica', '8ª', 'Ao saber que o antigo namorado ainda estava solteiro e em maus lençóis financeiros, Aurélia resolve se vingar do abandono sofrido e se propõe a comprá-lo. Os dois, por fim, casam-se.', 'idAutor')
    livros.excluir_livro(1)
    livros.ler_livro()
    