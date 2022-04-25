from django.db import models

# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=100)
    image = models.ImageField(upload_to = 'chefs/%Y/%m/%d/')
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'