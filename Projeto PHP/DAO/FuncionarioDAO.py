import pymysql
from Conexao import ConectarDb

class Funcionario:

    def inserir_funcionario(self, nome, email, telefone, login, senha):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "INSERT INTO funcionarios (nome, email, telefone, login, senha) VALUES (%s, %s, %s, %s, %s)"
            conexao.cursor.execute(sql, (nome, email, telefone, login, senha))
            conexao.conn.commit()
            print("Funcionario inserido com sucesso.")
        except pymysql.Error as e:
            print(f"Erro ao inserir funcionario: {e}")
        finally:
            conexao.desconectar()
        
    def ler_funcionario(self):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "SELECT * FROM funcionarios"
            conexao.cursor.execute(sql)
            funcionarios = conexao.cursor.fetchall()
            for funcionario in funcionarios:
                print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Email: {funcionario[2]}, Telefone: {funcionario[3]}, Login: {funcionario[4]}, Senha: {[5]}")
        except pymysql.Error as e:
            print(f"Erro ao ler funcionario: {e}")
        finally:
            conexao.desconectar()

    def atualizar_funcionario(self, matriculaFun, nome, email, telefone, login, senha):        
        conexao = ConectarDb()
        conexao.conectar()

        try:
            sql = "UPDATE funcionarios SET nome = %s, email = %s, telefone = %s, login = %s, senha =%s WHERE matriculaFun = %s;"
            conexao.cursor.execute(sql, (nome, email, telefone, login, senha, matriculaFun))
            conexao.conn.commit()
            print("Funcionario atualizado com sucesso.")

        except pymysql.Error as e:
            print(f"Erro ao atualizar funcionario: {e}")
    
    def excluir_funcionario(self, matriculaFun):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "DELETE FROM funcionarios WHERE matriculaFun = %s"
            conexao.cursor.execute(sql, (matriculaFun))
            conexao.conn.commit()
            print(f"Funcionario excluido com sucesso.")
        
        except pymysql.Error as e:
            print(f"Erro ao tentar excluir registro: {e}")

# Teste do código com os métodos CRUD
if __name__ == "__main__":

    funcionarios = Funcionario()
    
    funcionarios.atualizar_funcionario(1, 'Ricardo', 'firm@gmail.com', 87996110261, 'juca', 258)
    #funcionarios.atualizar_funcionario(3,'Antonio alves', 'marcelo@hotmail.com', 87911026154,'chaves', 147)
    
    funcionarios.ler_funcionario()
    