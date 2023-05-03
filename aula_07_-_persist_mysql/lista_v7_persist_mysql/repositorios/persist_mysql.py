import mysql.connector
import models.pessoa as mod
import uuid

class PersistMySQL:
    def __init__(self, host, user, password, database, table):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table

    def incluir_pessoa(self, pessoa):
        query = "INSERT INTO {} (nome, idade, cidade) VALUES ('{}', {}, '{}')".format(self.table, pessoa.nome, pessoa.idade, pessoa.cidade)
        self.executar_query(query)

    def alterar_pessoa(self, pessoa):
        query = "UPDATE {} SET idade = {}, cidade = '{}', nome = '{}' WHERE id = {}".format(self.table, pessoa.idade, pessoa.cidade, pessoa.nome, pessoa.id)
        self.executar_query(query)

    def excluir_pessoa(self, nome):
        query = "DELETE FROM {} WHERE id = '{}'".format(self.table, id)
        self.executar_query(query)

    def listar_pessoas(self):
        query = "SELECT nome, idade, cidade FROM {}".format(self.table)
        resultados = self.executar_query(query)
        lista_instancia_pessoas = []
        for resultado in resultados:
            pessoa = mod.Pessoa(nome=resultado[0], idade=resultado[1], cidade=resultado[2])
            lista_instancia_pessoas.append(pessoa)
        return lista_instancia_pessoas

    def executar_query(self, query):
        cnx = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        cursor = cnx.cursor()
        cursor.execute(query)
        if query.lower().startswith("select"):
            resultados = cursor.fetchall()
            cursor.close()
            cnx.close()
            return resultados
        else:
            cnx.commit()
            cursor.close()
            cnx.close()
