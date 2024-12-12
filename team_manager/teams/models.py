# teams/models.py


from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
     return f"{self.team1} vs {self.team2} on {self.date.strftime('%Y-%m-%d')}"

class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name