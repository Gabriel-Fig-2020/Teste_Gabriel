from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import ContatoForm, ProdutoModelForm
from .models import Curso


def index(request):
    context = {
        'cursos': Curso.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def curso(request):

    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()

            messages.success(request, 'Curso salvo com sucesso.')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar curso.')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }
    return render(request, 'cursos.html', context)
