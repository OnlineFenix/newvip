from django.db import models


# Create your models here.


class NewResult(models.Model):
    game_name = models.CharField(max_length=100)
    result = models.CharField(max_length=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.game_name} || {self.result}'


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class NewTag(models.Model):
    game_name = models.CharField(max_length=20)
    tag = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.game_name} || {self.tag}'


class Feedback(models.Model):
    username = models.CharField(max_length=100)
    feedback = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.username} || {self.feedback}'