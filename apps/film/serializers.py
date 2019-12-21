from rest_framework.serializers import ModelSerializer

from apps.film.models import Film


class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = ['film_id',
                  'title',
                  'description',
                  'release_year',
                  'rental_duration',
                  'rental_rate',
                  'length',
                  'replacement_cost',
                  'rating',
                  'last_update',
                  'special_features',
                  'fulltext']
