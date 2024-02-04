from django.db import models

class Socials(models.Model):
    link = models.TextField()
    name = models.CharField(max_length=100)