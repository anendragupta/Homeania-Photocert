from django.db import models
from django.contrib.auth.models import User

class Practical_test(models.Model):
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='C:\Users\guptaane\PycharmProjects\Homeania-Photocert\Homeania-Photocert\home\static\media',max_length=2000)

    def __str__(self):
        return self.description


class First_level(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.question


class Second_level(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.question

class Third_level(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.question

