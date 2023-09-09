# Importa o módulo viewsets do Django REST framework, que é usado para criar ViewSets.
# Também importa os modelos e serializadores necessários do seu aplicativo.
from rest_framework import viewsets
from todo.models import Tarefa
from todo.serializers.tarefaSerializer import TarefaSerializer


# Define uma classe chamada TarefaViewSet que herda de viewsets.ModelViewSet.
# Isso cria um ViewSet completo para o modelo Tarefa.
class TarefaViewSet(viewsets.ModelViewSet):
    # Define o queryset, que é o conjunto de consultas de objetos Tarefa.
    # Neste caso, estamos obtendo todos os objetos Tarefa no banco de dados.
    queryset = Tarefa.objects.all()
    # Define o serializer_class, especificando qual serializer deve ser usado
    # para serializar e desserializar objetos Tarefa.
    # Neste caso, estamos usando o TarefaSerializer que foi importado anteriormente.
    serializer_class = TarefaSerializer
