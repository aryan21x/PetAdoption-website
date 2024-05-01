from django.db import models

# Create your models here.
class Vet(models.Model):
    vet_id = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    phoneNumber = models.DecimalField(max_digits=10, decimal_places=2)
    businessName = models.CharField(max_length=255)