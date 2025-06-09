from django.db import models
from django.contrib.auth.models import User
#BY: SUBIA EDSON
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15) # <-- AÑADIDO
    # ... (resto de los campos de Venue)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, blank=True)
    def __str__(self):
        return self.name

# --- Añadiré los modelos del vídeo como réplica ---

class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=10)
    # Esta es la relación uno-a-muchos que nos muestra el video
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Simple(models.Model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')

    def __str__(self):
        return self.url

class DateExample(models.Model):
    the_date = models.DateTimeField()

class NullExample(models.Model):
    col = models.CharField(max_length=10, blank=True, null=True)
    
class Movie(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=120) # <-- AUMENTADO
    movies = models.ManyToManyField(Movie, blank=True)
    def __str__(self):
        return self.name
