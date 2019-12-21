from django.contrib import admin

# Register your models here.
from apps.film.models import Film

admin.site.register(Film)
