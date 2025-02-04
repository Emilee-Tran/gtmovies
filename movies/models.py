from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')

    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Review(models.Model):
    id = models.AutoField(primary_key=True) # automatically created id
    comment = models.CharField(max_length=255) # review text, max 255 chars
    date = models.DateTimeField(auto_now_add=True) # date review made
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # movie review is associated w/
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user that made review

    def __str__(self):
        return str(self.id) + ' - ' + self.move.name