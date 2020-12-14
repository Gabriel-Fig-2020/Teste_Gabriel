from django.contrib import admin

from .models import Curso

@admin.register(Curso)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','vagas','slug','criado','modificado','ativo')

# Register your models here.
