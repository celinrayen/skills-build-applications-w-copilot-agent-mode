# models.py for octofit_tracker
from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        abstract = True

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)
    class Meta:
        abstract = True

class Activity(models.Model):
    user = models.EmbeddedField(model_container=User)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        abstract = True

class Leaderboard(models.Model):
    team = models.EmbeddedField(model_container=Team)
    points = models.IntegerField()
    class Meta:
        abstract = True

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        abstract = True
