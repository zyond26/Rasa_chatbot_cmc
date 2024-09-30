from django.db import models

# Create your models here.
class Support(models.Model):
    question = models.TextField()
    reply = models.TextField()