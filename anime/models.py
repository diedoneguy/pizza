from django.db import models

# Create your models here.
class Cafe(models.Model):
    name = models.CharField(max_length=100)
    ingridients = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'cafe/%Y/%m/%d/')
    price = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

