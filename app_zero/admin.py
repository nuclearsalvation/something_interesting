from django.contrib import admin
from .models import ZeroModel

# Register your models here.
class ZeroModelAdmin(admin.ModelAdmin):
    list_display = 'fig'

admin.site.register(ZeroModel)