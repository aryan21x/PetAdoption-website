from django.db import models

class Adopter(models.Model):
    adopt_id = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255)
    pets = models.IntegerField()
    phoneNumber = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.fName} {self.lName}"

