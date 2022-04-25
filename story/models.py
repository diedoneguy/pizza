from django.db import models

# Create your models here.
class Story(models.Model):
    tag = models.CharField(max_length=100)
    story = models.TextField(max_length=100)
    image = models.ImageField(upload_to = 'story/%Y/%m/%d/')
    def __str__(self) -> str:
        return self.tag