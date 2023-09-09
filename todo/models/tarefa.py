from django.db import models
from .categoria import Categoria

# chamar a class categoria para poder trabalhar em tarefa


class Tarefa(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    # Bank diz que o campo pode ficar em branco e null que se nenhum dado for passado o db vai considerar como null
    creation_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    # Outros campos da tarefa como data de criação, data de conclusão, etc.

    def __str__(self):
        return self.title
