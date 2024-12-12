from django.db import models
class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='player_images/')  # Ensure this field is defined

    def __str__(self):
        return self.name
# Create your models here.
