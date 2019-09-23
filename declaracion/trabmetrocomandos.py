from django.contrib import admin
from models import  Template

from trix.admin import TrixAdmin

#admin.site.register(Template)

@admin.register(Template)
class PostAdmin(TrixAdmin, admin.ModelAdmin):
    trix_fields = ('content',)
