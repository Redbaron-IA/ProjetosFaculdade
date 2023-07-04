import pymysql
from Conexao import ConectarDb

class Emprestimo:

    def inserir_emprestimo(self, matriculaFun, matriculaUs, registro, dataEmprestimo, dataDevolucao):
        conexao = ConectarDb()
        conexao.conectar()

        try:
            # Verificar se os registros existem nas respectivas tabelas antes de fazer o empréstimo
            sql_check_usuario = "SELECT matriculaUs FROM usuarios WHERE matriculaUs = %s"
            conexao.cursor.execute(sql_check_usuario, (matriculaUs,))
            resultado_usuario = conexao.cursor.fetchone()

            sql_check_funcionario = "SELECT matriculaFun FROM funcionarios WHERE matriculaFun = %s"
            conexao.cursor.execute(sql_check_funcionario, (matriculaFun,))
            resultado_funcionario = conexao.cursor.fetchone()

            sql_check_livro = "SELECT registro FROM livros WHERE registro = %s"
            conexao.cursor.execute(sql_check_livro, (registro,))
            resultado_livro = conexao.cursor.fetchone()

            if resultado_usuario and resultado_funcionario and resultado_livro:
                # Todos os registros existem nas respectivas tabelas, podemos fazer o empréstimo
                sql_emprestimo = "INSERT INTO emprestimos (matriculaFun, matriculaUs, registro, dataEmprestimo, dataDevolucao) VALUES (%s, %s, %s, %s, %s)"
                conexao.cursor.execute(sql_emprestimo, (matriculaFun, matriculaUs, registro, dataEmprestimo, dataDevolucao))
                conexao.conn.commit()
                print("Empréstimo realizado com sucesso.")
            else:
                print("Erro ao inserir empréstimo: Algum dos registros não existe nas respectivas tabelas.")
        except pymysql.Error as e:
            print(f"Erro ao inserir empréstimo: {e}")
        finally:
            conexao.desconectar()

        
    def ler_emprestimo(self):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "SELECT * FROM emprestimos"
            conexao.cursor.execute(sql)
            emprestimos = conexao.cursor.fetchall()
            for row in emprestimos:
                print(f"ID: {row[0]}, Funcionario: {row[1]}, Usuario: {row[2]}, Livro: {row[3]}, Emprestimo: {row[4]}, Devolucão: {row[5]}")
        except pymysql.Error as e:
            print(f"Erro ao ler emprestimos: {e}")
        finally:
            conexao.desconectar()

    def atualizar_emprestimo(self, id_emprestimo, dataEmprestimo, dataDevolucao):        
        conexao = ConectarDb()
        conexao.conectar()

        try:
            sql = "UPDATE emprestimos SET dataEmprestimo = %s, dataDevolucao = %s WHERE id_emprestimo = %s"
            conexao.cursor.execute(sql, ( dataEmprestimo, dataDevolucao, id_emprestimo))
            conexao.conn.commit()
            print("Livro atualizado com sucesso.")

        except pymysql.Error as e:
            print(f"Erro ao atualizar livro: {e}")
    
    def excluir_emprestimo(self, id_emprestimo):
        conexao = ConectarDb()
        conexao.conectar()
        
        try:
            sql = "DELETE FROM emprestimos WHERE id_emprestimo = %s"
            conexao.cursor.execute(sql, (id_emprestimo))
            conexao.conn.commit()
            print(f"livros excluido com sucesso.")
        
        except pymysql.Error as e:
            print(f"Erro ao tentar excluir registro: {e}")

# Teste do código com os métodos CRUD
if __name__ == "__main__":
    emp = Emprestimo()
    
    #emp.inserir_emprestimo(3, 2, 3, 1409,2509)
    emp.atualizar_emprestimo(4,  22, 4)
    #emp.excluir_emprestimo(2)
    emp.ler_emprestimo()
    