import pymysql
from Conexao import ConectarDb

class Usuario:

    def inserir_usuario(self, nome, email, telefone):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "INSERT INTO usuarios (nome, email, telefone) VALUES (%s, %s, %s)"
            conexao.cursor.execute(sql, (nome, email, telefone))
            conexao.conn.commit()
            print("Usuario inserido com sucesso.")
        except pymysql.Error as e:
            print(f"Erro ao inserir usuario: {e}")
        finally:
            conexao.desconectar()
        
    def ler_usuario(self):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "SELECT * FROM usuarios"
            conexao.cursor.execute(sql)
            usuarios = conexao.cursor.fetchall()
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nome: {usuario[1]}")
        except pymysql.Error as e:
            print(f"Erro ao ler usuario: {e}")
        finally:
            conexao.desconectar()

    def atualizar_usuario(self, matriculaUs, nome, email, telefone):        
        conexao = ConectarDb()
        conexao.conectar()

        try:
            sql = "UPDATE usuarios SET nome = %s, email = %s, telefone = %s WHERE matriculaUs = %s"
            conexao.cursor.execute(sql, (matriculaUs, nome, email, telefone))
            conexao.conn.commit()
            print("Usuario atualizado com sucesso.")

        except pymysql.Error as e:
            print(f"Erro ao atualizar usuario: {e}")
    
    def excluir_usuario(self, matriculaUs):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "DELETE FROM usuarios WHERE matriculaUs = %s"
            conexao.cursor.execute(sql, (matriculaUs))
            conexao.conn.commit()
            print(f"Usuario excluido com sucesso.")
        
        except pymysql.Error as e:
            print(f"Erro ao tentar excluir registro: {e}")

# Teste do código com os métodos CRUD
if __name__ == "__main__":

    usuarios = Usuario()
    usuarios.atualizar_usuario( 1, 'Ricardo', 'firm@gmail.com', 87996110261)
    usuarios.atualizar_usuario(3,'Antonio alves', 'marcelo@hotmail.com', 87911026154)
    usuarios.excluir_usuario(4)
    
    usuarios.ler_usuario()
    