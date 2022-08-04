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


