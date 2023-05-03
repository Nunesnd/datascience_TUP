import csv
import os
import models.pessoa as mod

class PersistCSV:
    def __init__(self, nome_arquivo):
        caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.arquivo = os.path.join(caminho_projeto, "data", nome_arquivo)
        self.campos = ["nome", "idade", "cidade"]
        self.pessoas = []

    def incluir_pessoa(self, pessoa):
        self.carregar_dados()
        self.pessoas.append(pessoa.__dict__)
        self.salvar_dados()

    def alterar_pessoa(self, pessoa):
        self.carregar_dados()
        for i, p in enumerate(self.pessoas):
            if p["nome"] == pessoa.nome:
                self.pessoas[i] = pessoa.__dict__
                self.salvar_dados()
                break

    def excluir_pessoa(self, nome):
        self.carregar_dados()
        self.pessoas = [p for p in self.pessoas if p["nome"] != nome]
        self.salvar_dados()

    def listar_pessoas(self):
        self.carregar_dados()
        lista_instancia_pessoas = []
        for p in self.pessoas:
            pessoa = mod.Pessoa(**p)
            lista_instancia_pessoas.append(pessoa)
        return lista_instancia_pessoas

    def carregar_dados(self):
        try:
            with open(self.arquivo, "r", newline='') as f:
                reader = csv.DictReader(f, fieldnames=self.campos)
                next(reader) #ignorar primeira linha
                for row in reader:
                    self.pessoas.append(row)
        except FileNotFoundError:
            self.pessoas = []

    def salvar_dados(self):
        with open(self.arquivo, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.campos)
            writer.writeheader()
            for pessoa in self.pessoas:
                writer.writerow(pessoa)
