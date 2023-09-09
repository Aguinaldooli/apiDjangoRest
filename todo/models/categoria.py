from django.db import models


class Categoria(models.Model):
    opcoes = [
        (1, "Hobby"),
        (2, "Saúde"),
        (3, "Tarefas de Casa"),
    ]

    def lista_opcoes(self):
        return [opcao[1] for opcao in self.opcoes]

    def __str__(self):
        return dict(self.opcoes)[self.id]
