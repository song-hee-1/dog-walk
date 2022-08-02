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
    def get_walk(self, request, **kwargs):
        if self.request.method == 'GET':
            obj_id = self.kwargs['pk']
            walk = Walk.objects.filter(pet_id=obj_id)
            serializer = WalkSerializer(walk, many=True)
            return Response(serializer.data)
        elif self.request.method == 'POST':
            serializer = WalkSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'new walklog set'})
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
