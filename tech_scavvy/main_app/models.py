from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Judge(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Player(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # designates team leader.. can only be one per team
    leader = models.BooleanField()

    def __str__(self):
        return f"{self.name} on team {self.team}"


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    winner = models.BooleanField()
    team_id = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Task(model.Models):
    task = models.CharField(max_length=100)
    team1_complete = models.BooleanField(default='False')
    team2_complete = models.BooleanField(default='False')
    # this allows each task that is needed in a given match to have the many to one with team 1 and team 2
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE)

    # this allows us to know the order of the tasks and programatically work on them in that order
    task_number = models.IntegerField(default=-1)

    def new_game_reset(self):
        self.team1
        self.team1_complete = 'False'
        self.team2
        self.team2_complete = 'False'
        self.task_number = -1
