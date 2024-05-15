from django.db import models

class medkit(models.Model):
    MedicineName = models.CharField(max_length=500)
    Quantity = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    ExpirationDate = models.CharField(max_length=500)


class searchb(models.Model):
    medname = models.CharField(max_length=500)