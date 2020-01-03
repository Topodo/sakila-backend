from django.db import models
from apps.film.models import Film


# Create your models here.

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now_add=True, blank=True)
    films = models.ManyToManyField(Film)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        managed = False
        db_table = 'actor'
