from rest_framework import serializers

from .models import Owner, Pet, Walk


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class WalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walk
        fields = '__all__'
