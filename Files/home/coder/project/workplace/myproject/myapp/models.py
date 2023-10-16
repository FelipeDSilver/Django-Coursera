from django.db import models

class Drinks(models.Model):
    drink_name = models.Charfield(max_length=200)
    price = models.integerfield()
