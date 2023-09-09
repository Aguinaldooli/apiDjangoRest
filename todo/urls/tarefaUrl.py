from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin
from todo.views.tarefaViewSets import TarefaViewSet

# Cria um objeto de roteador padrão para ViewSets.
router = DefaultRouter()
router.register(r"tarefas", TarefaViewSet)

# Define as URLs do aplicativo 'todo'.
urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/", include("todo.urls.tarefaUrl")
    ),  # Inclui as URLs do aplicativo 'todo'.
]

urlpatterns = router.urls
