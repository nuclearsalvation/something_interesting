from django.contrib import admin
from .models import ZeroModel, ZeroImageModel, ZeroCSVModel, ZeroNameNumModel, ZeroStringModel

# Register your models here.
class ZeroModelAdmin(admin.ModelAdmin):
    list_display = 'fig'

admin.site.register(ZeroModel)
admin.site.register(ZeroImageModel)
admin.site.register(ZeroCSVModel)
admin.site.register(ZeroNameNumModel)
admin.site.register(ZeroStringModel)