from django.db import models

class Practical_test(models.Model):
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='\Users\guptaane\PycharmProjects\homeania\home\static\media')