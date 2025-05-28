from django.db import models
from django_matplotlib.fields import MatplotlibFigureField

# Create your models here.

class ZeroModel(models.Model):
    fig = MatplotlibFigureField(figure = 'sin_figure')
