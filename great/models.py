from django.db import models

# Create your models here.
class Great(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField(max_length=100)
    price  = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Great'
        verbose_name_plural = 'Greats'
