from django.db import models

class AssociatedBusiness(models.Model):
    business_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    service = models.CharField(max_length=255, null=True, blank=True)
    phoneNumber = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
