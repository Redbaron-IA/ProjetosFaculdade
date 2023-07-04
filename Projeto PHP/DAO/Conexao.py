import pymysql

class ConectarDb:
    def __init__(self):
        self.dbProjeto = 'dbProjeto'
        self.host = 'localhost'
        self.user = 'admin'
        self.passwd = 'linkpe'
        self.conn = None
        self.cursor = None
    
    def conectar(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.dbProjeto)
            self.cursor = self.conn.cursor()
            print("Conexão com o banco de dados estabelecida.")
        except pymysql.Error as e:
            print(f"Erro ao conectar-se ao banco de dados: {e}")
    
    def desconectar(self):
        if self.conn:
            self.conn.close()
            print("Conexão com o banco de dados encerrada.")
        
   