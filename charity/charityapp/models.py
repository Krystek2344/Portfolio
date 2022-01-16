from django.db import models
from django.contrib.auth.models import User

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


class Donation(models.Model):
    quantity = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=155)
    phone_number = models.CharField(max_length=25)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=12)
    pick_up_date = models.DateTimeField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
