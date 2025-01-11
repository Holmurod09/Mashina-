from django.db import models

class Auto(models.Model):
    logo = models.ImageField(upload_to='media/auto')
    title = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.IntegerField()
    background = models.ImageField(upload_to='media/auto')
    mator = models.CharField(max_length=100)
    benzin = models.CharField(max_length=100)
    uzatma = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Buyur(models.Model):
    background = models.ImageField(upload_to='media/buyur')
    

