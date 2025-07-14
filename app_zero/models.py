from django.db import models
from django_matplotlib.fields import MatplotlibFigureField

# Create your models here.

class ZeroModel(models.Model):
    fig = MatplotlibFigureField(figure = 'sin_figure', plt_args=(2,5000,2,0.001))

class ZeroImageModel(models.Model):
    img = models.ImageField()

class ZeroStringModel(models.Model):
    source = models.TextField()

class ZeroCSVModel(models.Model):
    file = models.FileField()

class ZeroNameNumModel(models.Model):
    name = models.TextField()
    num = models.FloatField()

class ZeroJSONModel(models.Model):
    list = models.JSONField(default=dict,blank=True)