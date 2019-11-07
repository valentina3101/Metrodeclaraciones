from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import edit
from .models import Declaracion, Template
from .forms import DeclaracionForm
from django.conf import settings
import os

from django_weasyprint import WeasyTemplateResponseMixin


class BaseView(LoginRequiredMixin):
    model = Declaracion
    form_class = DeclaracionForm
    template_name = 'base.html'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        grupos_del_user = self.request.user.groups.all()
        templates_del_user = Template.objects.filter(groups__in=grupos_del_user).distinct()
        form.fields['template'].choices = [(t.id, str(t)) for t in templates_del_user]
        return form


class ListView(BaseView, generic.ListView):
    template_name = 'declaracion/list.html' # 'declaracion/list.html'
    paginate_by = 10


class CreateView(BaseView, edit.CreateView):
    template_name = 'declaracion/form.html'

    def form_valid(self, form):
        messages.info(self.request, 'Declaración «{}» creada correctamente'.format(form.instance.título))
        form.instance.cargado_por = self.request.user
        return super(CreateView, self).form_valid(form)


class UpdateView(BaseView, edit.UpdateView):
    template_name = 'declaracion/form.html'

    def form_valid(self, form):
        messages.info(self.request, 'Declaración «{}» modificada correctamente'.format(form.instance.título))
        return super(UpdateView, self).form_valid(form)


class DeclaracionHTML(generic.DetailView):
    model = Declaracion

    def get_template_names(self):
        declaracion=self.get_object()
        plantilla = os.path.join(settings.BASE_DIR, 'pdf_templates', 'declaracion.html')
        # acá escribimos el contenido "editable" del template en un archivo
        open(plantilla, 'w').write(declaracion.template.contenido + declaracion.template.pie)
        return [plantilla]



class DeclaracionPDF(WeasyTemplateResponseMixin, DeclaracionHTML):
    pass


class DeclaracionPNG(DeclaracionPDF):
	content_type = 'image/png'
