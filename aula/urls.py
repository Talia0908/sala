from django.urls import path
from . import views

urlpatterns = [
    path('aluno/', views.home),
    path('aluno/show/<int:id>', views.aluno_show),
    path('aluno/list', views.aluno_list),
    path('aluno/create/', views.create),
    path('aluno/<int:id>/', views.delete),
    path('aluno/editar/<int:id>', views.editar),
]