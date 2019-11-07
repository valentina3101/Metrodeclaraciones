from datetime import date
from django.db import models
from django.conf import settings
from django.urls import reverse
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices
from trix.fields import TrixField


class Declaracion(models.Model):
    ESTADOS = Choices('borrador', 'publicado')
    #CHOICE_PLANTILLA = Choices('cecilia', 'default')
    fecha_publicacion = MonitorField(monitor='estado', when=['publicado'], editable=False)
    cargado_por = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE)

    título = models.CharField(max_length=100)
    fecha = models.DateField(default=date.today())
    declaración = TrixField()

    estado = StatusField(choices_name='ESTADOS')
    nota_interna = models.TextField(blank=True, null=True)

    #opcion_plantilla = StatusField(choices_name='CHOICE_PLANTILLA')

    template = models.ForeignKey('Template', null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('estado', '-fecha', '-id')

'''
class Template(models.Model):
	nombre = models.CharField(max_length=100)
	archivo =  models.FileField(upload_to='')

	def __str__(self):
		return self.nombre
'''
#agrego esta clase
class Template(models.Model):
    nombre = models.CharField(max_length=100,)
    contenido = models.TextField()
    #contenido_extra = TrixField()
    pie = models.TextField()
    groups = models.ManyToManyField("auth.Group")
    

    def __str__(self):
        return self.nombre
