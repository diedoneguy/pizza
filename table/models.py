import email
from tabnanny import verbose
from django.db import models
# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    seats = models.IntegerField()

    def __str__(self) -> str:
        return self.phone
    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'