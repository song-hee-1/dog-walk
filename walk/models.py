from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'owner'


class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    breed = models.CharField(max_length=15, null=False)
    birth = models.DateField(null=False)
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pet'


class Walk(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(null=False)
    distance = models.CharField(max_length=20)

    def __str__(self):
        return self.time

    class Meta:
        db_table = 'walk'
