from django.db import models
from django_mysql.models import ListCharField

# Create your models here.

class Audiobase(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name
    

class Song(Audiobase):
    pass
    
class Podcast(Audiobase):
    host = models.CharField(max_length=100)
    participants = ListCharField(
        null=True,
        blank=True,
        base_field=models.CharField(max_length=100),
        size = 10,
        max_length=(10 * 100)+10,
    )

class Audiobook(Audiobase):
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
