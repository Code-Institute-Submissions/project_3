from django.db import models

# Create your models here.
class MainGenre(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.FileField(upload_to='images/main/')
    
    def __str__(self):
        return self.name
        
class SubGenre(models.Model):
    dom = models.ForeignKey('MainGenre', related_name="MainGenre", default='')
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.FileField(upload_to='images/main/')
    
    def __str__(self):
        return self.name
        