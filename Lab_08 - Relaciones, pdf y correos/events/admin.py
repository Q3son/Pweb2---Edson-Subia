from django.contrib import admin

# En esta parte, añadiremos los nuevos modelos a la importación
from .models import Venue, Event, Language, Framework, Simple, DateExample, NullExample, Movie, Character

# Y registramos los modelos originales (cree dos extra para mis propios experimentos y personalización)
admin.site.register(Venue)
admin.site.register(Event)

# También registramos los modelos del vídeo
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Simple)
admin.site.register(DateExample)
admin.site.register(NullExample)
admin.site.register(Movie)
admin.site.register(Character)