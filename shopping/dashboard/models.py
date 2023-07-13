from django.db import models


class ElectronicItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    price = models.FloatField()

    def __str__(self):
        return self.name
