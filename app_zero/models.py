from django.db import models
from django_matplotlib.fields import MatplotlibFigureField

# Create your models here.

class ZeroModel(models.Model):
    fig = MatplotlibFigureField(figure = 'sin_figure', plt_args=(2,5000,2,0.001))

class ZeroImageModel(models.Model):
    img = models.ImageField()

class ZeroStringModel(models.Model):
    source = models.TextField()