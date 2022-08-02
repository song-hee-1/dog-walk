from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Pet, Walk
from .serializers import PetSerializer, WalkSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    @action(detail=False, methods=['GET', 'POST'], url_path="^(?P<pk>[^/.]+)/walk", serializer_class=WalkSerializer)
    def walk(self, request, **kwargs):
        obj_id = self.kwargs['pk']
        walk = Walk.objects.filter(pet_id=obj_id)
        serializer = WalkSerializer(walk, many=True)
        return Response(serializer.data)
