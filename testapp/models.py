from django.db import models

# Create your models here.
class productMainModel(models.Model):
    qChoice = (("high", "h"), ("low", "l"), ("medium", "m"))
    noChoice = ((10, "1"), (20, "2"), (30, "3"))
    title = models.CharField(max_length=300, blank=True, null = True)
    Description = models.CharField(max_length=500, blank=True, null = True)
    Price = models.IntegerField(blank=True, null = True)
    unique_code = models.TextField(unique=True, null = False)
    Size = models.IntegerField(choices=noChoice)
    Quality = models.CharField(max_length=50, choices=qChoice)

class productColourModel(models.Model):
    cChoice = (("red", "r"), ("blue", "b"), ("green", "g"), ("black", "b"))
    Product = models.ForeignKey( "productMainModel", on_delete=models.CASCADE)
    Colour = models.CharField(max_length=50, choices=cChoice)

class productImageModel(models.Model):
    Product = models.ForeignKey( "productMainModel", on_delete=models.CASCADE)
    Image = models.ImageField(blank=True, null = True)
