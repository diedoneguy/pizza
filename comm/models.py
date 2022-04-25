from django.db import models

# Create your models here.
class Comments(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=100)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'coment/%Y/%m/%d/')
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'