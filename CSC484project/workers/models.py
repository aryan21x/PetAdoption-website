from django.db import models

# Create your models here.
class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    shelter_id = models.ForeignKey('Shelter', on_delete=models.CASCADE)
    
    class Meta:
        indexes = [
            models.Index(fields=['shelter_id']),
        ]