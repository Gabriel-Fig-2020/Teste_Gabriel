from django.urls import path

from .views import index, contato, curso

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('cursos/', curso, name='cursos'),
]