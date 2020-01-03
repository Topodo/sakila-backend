from django.urls import path
from apps.actor.views import ListActors, DetailActors, FilmsOfTheActor, BindFilmToActor, CreateActor

urlpatterns = [
    path('actors/', ListActors.as_view()),
    path('actors/<int:pk>/', DetailActors.as_view()),
    path('actors/<int:pk>/films/', FilmsOfTheActor.as_view()),
    path('actors/<int:actor_id>/films/<int:film_id>/', BindFilmToActor.as_view()),
    path('actors/new/', CreateActor.as_view())
]