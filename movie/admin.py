from django.contrib import admin

# Para registrar modelos en la vista de admin
from .models import Movie
admin.site.register(Movie)