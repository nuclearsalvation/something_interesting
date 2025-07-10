from django.db import models

# Create your models here.

class FunctionsTaylorSeriesModel(models.Model):
    c0 = models.FloatField()
    c1 = models.FloatField()
    c2 = models.FloatField()
    c3 = models.FloatField()
    c4 = models.FloatField()
    c5 = models.FloatField()
    c6 = models.FloatField()
    c7 = models.FloatField()
    c8 = models.FloatField()
    x0 = models.FloatField()
    name = models.CharField(max_length=20)
    description = models.TextField()

class FunctionFourierSeriesModel(models.Model):
    a0 = models.FloatField()
    a1 = models.FloatField()
    a2 = models.FloatField()
    a3 = models.FloatField()
    a4 = models.FloatField()
    b1 = models.FloatField()
    b2 = models.FloatField()
    b3 = models.FloatField()
    b4 = models.FloatField()
    l = models.FloatField()
    name = models.CharField(max_length=20)
    description = models.TextField()