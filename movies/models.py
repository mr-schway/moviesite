from django.db import models

# Create your models here.
class Movies(models.Model):
  name = models.CharField(max_length=200)
  rating = models.FloatField(default=0)

  def __str__(self):
    return self.name