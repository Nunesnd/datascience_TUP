import pyodbc
import models.pessoa as mod

class PersistSqlServer:
    def __init__(self, server, database, username, password, table):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.table = table

    def incluir_pessoa(self, pessoa):
        query = f"INSERT INTO {self.table} (nome, idade, cidade) VALUES ('{pessoa.nome}', {pessoa.idade}, '{pessoa.cidade}')"
        self.executar_query(query)

    def alterar_pessoa(self, pessoa):
        query = f"UPDATE {self.table} SET idade = {pessoa.idade}, cidade = '{pessoa.cidade}', nome = '{pessoa.nome}' WHERE id = {pessoa.id}"
        self.executar_query(query)

    def excluir_pessoa(self, id):
        query = f"DELETE FROM {self.table} WHERE id = {id}"
        self.executar_query(query)

    def listar_pessoas(self):
        query = f"SELECT nome, idade, cidade FROM {self.table}"
        resultados = self.executar_query(query)
        lista_instancia_pessoas = []
        for resultado in resultados:
            pessoa = mod.Pessoa(nome=resultado[0], idade=resultado[1], cidade=resultado[2])
            lista_instancia_pessoas.append(pessoa)
        return lista_instancia_pessoas

    def executar_query(self, query):
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        )
        cursor = conn.cursor()
        cursor.execute(query)
        if query.lower().startswith("select"):
            resultados = cursor.fetchall()
            cursor.close()
            conn.close()
            return resultados
        else:
            conn.commit()
            cursor.close()
            conn.close()
