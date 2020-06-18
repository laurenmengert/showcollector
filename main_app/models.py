from django.db import models

# Create your models here.


class Show(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    num_seasons = models.IntegerField()
    description = models.TextField(max_length=300)
    imdb_rating = models.IntegerField()
    
    def __str__(self):
        return self.name