from django.http import Http404
from rest_framework import generics, views, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from apps.actor.models import Actor
from apps.actor.serializers import ActorSerializer
from apps.film.models import Film
from apps.film.serializers import FilmSerializer

# Classes that extends from Django RESTFramework and contains the utils for CRUD operations in Film's model

"""
    /api/v1/films/
    GET Method that gets all Films from database
"""


class ListFilms(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'
    ordering = ['title']


"""
    /api/v1/films/{Film_id}/
    GET Method that get the data from an specific Film
"""


class DetailFilm(views.APIView):

    @staticmethod
    def get_object(pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        film = self.get_object(pk)
        serializer = FilmSerializer(film)
        return Response(serializer.data)


"""
    /api/v1/films/{Film_id}/actors/
    GET Method that get all Actors of an specific Film
"""


class ActorsOfTheFilm(generics.ListAPIView):
    serializer_class = ActorSerializer

    def get_queryset(self):
        # Gets the Film_id from URL params
        film_id = self.kwargs['pk']
        return Film.objects.get(pk=film_id).actor_set.order_by('last_name')


"""
    /api/v1/films/{film_id}/actors/{actor_id}
    POST Method that binds an Actor to the current Film
"""


class BindActorToFilm(views.APIView):
    @staticmethod
    def get_actor(pk):
        try:
            return Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            raise Http404

    @staticmethod
    def get_film(pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404

    def post(self, request, film_id, actor_id, format=None):
        film = self.get_film(pk=film_id)
        actor = self.get_actor(pk=actor_id)
        film.actor_set.add(actor)
        serializer = FilmSerializer(film)
        return Response(serializer.data)
