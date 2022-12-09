from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(blank=True, max_length=120)
    quantity = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
