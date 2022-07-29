from django.db import models


class Pet(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    breed = models.CharField(max_length=30, null=False)
    birth = models.DateField(null=False)
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pet'


class Walk(models.Model):
    pet = models.ForeignKey('pet.Pet', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(null=False)
    distance = models.CharField(max_length=20)

    def __str__(self):
        return self.time

    class Meta:
        db_table = 'walk'
