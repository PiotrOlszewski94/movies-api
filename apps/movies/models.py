from django.db import models

# Create your models here.
class Movie(models.Model):
    Title = models.CharField(max_length=1000)
    Year = models.PositiveIntegerField()
    Rated = models.CharField(max_length=255, blank=True)
    Released = models.CharField(max_length=255, blank=True)
    Runtime = models.CharField(max_length=255, blank=True)
    Genre = models.CharField(max_length=500, blank=True)
    Director = models.CharField(max_length=500, blank=True)
    Writer = models.CharField(max_length=500, blank=True)
    Actors = models.CharField(max_length=1000, blank=True)
    Plot = models.TextField(blank=True)
    Language = models.CharField(max_length=255, blank=True)
    Country = models.CharField(max_length=255, blank=True)
    Awards = models.CharField(max_length=1000, blank=True)
    Poster = models.CharField(max_length=1000, blank=True)
    Ratings = models.JSONField(default=list)
    Metascore = models.CharField(max_length=255, blank=True)
    imdbRating = models.CharField(max_length=255, blank=True)
    imdbVotes = models.CharField(max_length=255, blank=True)
    imdbID = models.CharField(max_length=255, blank=True)
    DVD = models.CharField(max_length=255, blank=True)
    BoxOffice = models.CharField(max_length=255, blank=True)
    Production = models.CharField(max_length=255, blank=True)
    Website = models.CharField(max_length=255, blank=True)

    # override save method to catch situation for Movie and movie
    def save(self, *args, **kwargs):
        for field_name in ['Title']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.title())
        super(Movie, self).save(*args, **kwargs)