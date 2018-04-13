from django.db import models

# Create your models here.
class MainGenre(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.FileField(upload_to='images/main/')
    
    def __str__(self):
        return self.name
        
class SubGenre(models.Model):
    genre = models.ForeignKey('MainGenre', related_name="subgenres", default='')
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.FileField(upload_to='images/main/')
    
    def __str__(self):
        return self.name

class Artists(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.FileField(upload_to='images/main/')
    genre = models.ManyToManyField(MainGenre, related_name="artists", help_text="Hold down 'Control', or 'Command' on a Mac, to select more than one.")
    subgenre = models.ManyToManyField(SubGenre, blank=True, related_name="artists", help_text="Hold down 'Control', or 'Command' on a Mac, to select more than one.")
    
    def __str__(self):
        return self.name