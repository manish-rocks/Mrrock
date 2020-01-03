from django.db import models

# Create your models here.
####Models for Cakes####
class Cake_Category(models.Model):
    cake_category = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    available_on_app = models.BooleanField(default=True)
    available_on_web = models.BooleanField(default=True)
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.cake_category