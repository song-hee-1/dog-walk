from django.db import models


class Walk(models.Model):
    pet = models.ForeignKey('pet.Pet', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(null=False)
    distance = models.CharField(max_length=20)

    def __str__(self):
        return self.time

    class Meta:
        db_table = 'walk'
