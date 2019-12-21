from django.http import Http404
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response

from apps.actor.models import Actor
from apps.actor.serializers import ActorSerializer
from apps.film.models import Film
from apps.film.serializers import FilmSerializer

# Classes that extends from Django RESTFramework and contains the utils for CRUD operations in Actor's model

"""
    /api/v1/actors/
    GET Method that gets all Actors from database
"""


class ListActors(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


"""
    /api/v1/actors/{actor_id}/
    GET Method that get the data from an specific Actor
"""


class DetailActors(views.APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)


"""
    /api/v1/actors/{actor_id}/films/
    GET Method that get all Films where an specific Actor has performed
"""


class FilmsOfTheActor(generics.ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        # Gets the actor_id from URL params
        actor_id = self.kwargs['pk']
        return Actor.objects.get(pk=actor_id).films


"""
    /api/v1/actors/{actor_id}/films/{film_id}
    POST Method that binds a Film to the current Actor
"""


class BindFilmToActor(views.APIView):
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

    def post(self, request, actor_id, film_id, format=None):
        film = self.get_film(pk=film_id)
        actor = self.get_actor(pk=actor_id)
        actor.films.add(film)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)