from django.db import models


# Create your models here.
class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_update = models.DateTimeField(auto_now_add=True, blank=True)
    special_features = models.TextField(blank=True, null=True)  # This field type is a guess.
    language_id = models.SmallIntegerField(default=1, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'film'
