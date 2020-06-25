from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

RATINGS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10')
)

# I know that the above ratings two tuple is probably unnecessary (or may not even make sense) but it worked and I
# did not have time to really play around and research another way to pre-set ratings, so if someone wants to give 
# me some advice on that, I would definitely take it!
class Performer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('performers_detail', kwargs={'pk': self.id})


class Show(models.Model): 
    name = models.CharField(max_length=100)
    num_seasons = models.IntegerField()
    description = models.TextField(max_length=500)
    imdb_rating = models.FloatField()
    performers = models.ManyToManyField(Performer)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'show_id': self.id})


class Review(models.Model):
    review_content = models.TextField(max_length=1000)
    date = models.DateField('Review Date')
    rating = models.CharField(
        max_length=5,
        choices=RATINGS,
        default=RATINGS[4][0]
    )
    
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'This review was written on {self.date}'
    
    class Meta:
        ordering = ['-date']