from django.db import models

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=33)
    description = models.CharField(max_length=233)
    image = models.ImageField(upload_to="media/")
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title