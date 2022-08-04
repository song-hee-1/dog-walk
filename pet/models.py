from django.db import models


class Pet(models.Model):
    owner_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE, db_column='owner_id')
    breed = models.CharField(max_length=30, null=False)
    birth = models.DateField(null=False)
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pet'
