from django.db import models

class Shelter(models.Model):
    shelter_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    pets = models.IntegerField(default=0)
    phoneNumber = models.DecimalField(max_digits=10, decimal_places=0)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name