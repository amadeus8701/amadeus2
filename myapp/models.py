from django.db import models

class Image(models.Model):
    path = models.CharField(max_length=255)