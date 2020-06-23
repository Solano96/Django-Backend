from rest_framework import serializers
from visitas_granada.models import Visita, Comentario


class VisitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visita
        fields = ('pk', 'nombre', 'descripcion', 'likes', 'foto')


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ('visita', 'texto')
