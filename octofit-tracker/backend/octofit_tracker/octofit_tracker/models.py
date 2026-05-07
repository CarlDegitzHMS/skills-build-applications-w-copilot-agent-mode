from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams', blank=True)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    date = models.DateField()

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return f"{self.user.name} - {self.activity_type}"


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return f"{self.user.name} - {self.score}"


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    exercises = models.JSONField(default=list)

    class Meta:
        app_label = 'octofit_tracker'

    def __str__(self):
        return self.name
