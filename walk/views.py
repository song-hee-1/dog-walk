from rest_framework import viewsets

from .models import Walk
from .serializers import WalkSerializer


class WalkViewSet(viewsets.ModelViewSet):
    queryset = Walk.objects.all().order_by('date', 'time')
    serializer_class = WalkSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'pet_id' in self.request.GET:
            queryset = queryset.filter(pet_id__in=self.request.GET.getlist('pet_id'))
        if 'owner_id' in self.request.GET:
            queryset = queryset.filter(pet_id__owner_id__in=self.request.GET.getlist('owner_id'))
        return queryset
