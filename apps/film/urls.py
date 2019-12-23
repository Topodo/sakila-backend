from django.urls import path

from apps.film.views import ListFilms, DetailFilm, ActorsOfTheFilm, BindActorToFilm

urlpatterns = [
    path('films/', ListFilms.as_view()),
    path('films/<int:pk>/', DetailFilm.as_view()),
    path('films/<int:pk>/actors/', ActorsOfTheFilm.as_view()),
    path('films/<int:film_id>/actors/<int:actor_id>/', BindActorToFilm.as_view())
]