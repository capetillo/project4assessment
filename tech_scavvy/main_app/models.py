from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  team = models.ForeignKey(Team, on_delete=models.CASCADE)
  #designates team leader.. can only be one per team
  leader = models.BooleanField()

  def __str__(self):
    return f"{self.name} on team {self.team}"
  
class Team(model.Model):
  team_name = models.CharField(max_length=100)
  winner = models.BooleanField()
  team_id = models.IntegerField()

  def __str__(self):
    return f"{self.name}"

class Judge(model.Models):
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(model.Models):
  task = models.CharField(max_length=100)
  team1_complete = models.BooleanField(default='False')
  team2_complete = models.BooleanField(default='False')


  