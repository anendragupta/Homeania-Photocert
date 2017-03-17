from django.db import models

class Practical_test(models.Model):
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='C:\Users\guptaane\PycharmProjects\Homeania-Photocert\Homeania-Photocert\home\static\media',max_length=2000)

    def __str__(self):
        return self.description


class First_Level(models.Model):
    question = models.CharField(max_length=200)
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200)
    ans4 = models.CharField(max_length=200)
    correct_ans = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.question

class Second_Level(models.Model):
    question = models.CharField(max_length=200)
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200)
    ans4 = models.CharField(max_length=200)
    correct_ans = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.question

class Third_Level(models.Model):
    question = models.CharField(max_length=200)
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200)
    ans4 = models.CharField(max_length=200)
    correct_ans = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.question


