from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Pet, Walk
from .serializers import PetSerializer, WalkSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    @action(detail=False, methods=['GET', 'POST'], url_path="^(?P<pet_id>[^/.]+)/walk", serializer_class=WalkSerializer)
    def get_walk(self, request, **kwargs):
        if self.request.method == 'GET':
            obj_id = self.kwargs['pet_id']
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

    @action(detail=True, methods=['GET', 'PUT', 'DELETE'],
            serializer_class=WalkSerializer, url_path=r'walk/(?P<walk_id>\d+)')
    def walk_detail(self, request, pk, **kwargs):
        if self.request.method == 'GET':
            pet_id = self.kwargs['pk']
            walk_id = self.kwargs['walk_id']
            walk = Walk.objects.filter(pet_id=pet_id, id=walk_id)
            serializer = WalkSerializer(walk, many=True)
            return Response(serializer.data)
        elif self.request.method == 'PUT':
            walk_data = JSONParser().parse(request)
            serializer = WalkSerializer(data=walk_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)
        elif self.request.method == 'DELTE':
            pass
