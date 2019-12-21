from django.contrib import admin

# Register your models here.
from apps.actor.models import Actor

admin.site.register(Actor)
