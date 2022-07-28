from django.http import HttpResponse

from rest_framework import viewsets

from .models import Walk
from .serializers import WalkSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the walk test.")


class WalkViewSet(viewsets.ModelViewSet):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer
