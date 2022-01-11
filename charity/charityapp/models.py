from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Institution(models.Model):
    CHOICES = (
        (1, "Fundacja"),
        (2, "Organizacja pozarządowa"),
        (3, "Zbiórka lokalna"),
        (4, "Domyślnie fundacja"),
    )
    name = models.CharField(max_length=125)
    description = models.TextField(max_length=275)
    type = models.BooleanField(CHOICES)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
