from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=233, verbose_name="Book title")
    description: models.TextField
    date_published: models.DateField(auto_now_add=True)
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    genre = 