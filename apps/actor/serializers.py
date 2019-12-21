from rest_framework.serializers import ModelSerializer
from apps.actor.models import Actor


class ActorSerializer(ModelSerializer):

    class Meta:
        model = Actor
        fields = ['actor_id',
                  'first_name',
                  'last_name',
                  'last_update']
