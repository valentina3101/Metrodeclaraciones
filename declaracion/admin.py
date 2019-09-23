from django.contrib import admin
from .models import Template
from trix.admin import TrixAdmin
from django_summernote.admin import SummernoteModelAdmin

#admin.site.register(Template)
@admin.register(Template)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
