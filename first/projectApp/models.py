from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    #image = models.ImageField(upload_to='project_images/')
    url = models.URLField(blank=True)