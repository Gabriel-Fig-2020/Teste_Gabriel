from django.db import models
from stdimage.models import StdImageField
# Create your models here.
# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Curso(Base):
    nome = models.CharField('CURSO', max_length=100)
    preco = models.DecimalField('PREÇO', max_digits=8, decimal_places=2)
    vagas = models.IntegerField('VAGAS')
    imagem = StdImageField('Imagem', upload_to='curso', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

#SLUG --> front end = front-end
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Curso)
