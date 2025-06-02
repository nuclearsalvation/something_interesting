from django.contrib import admin
from .models import ZeroModel, ZeroImageModel

# Register your models here.
class ZeroModelAdmin(admin.ModelAdmin):
    list_display = 'fig'

admin.site.register(ZeroModel)
admin.site.register(ZeroImageModel)