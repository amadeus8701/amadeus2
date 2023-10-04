from django.db import models

class UserInputmodel(models.Model):
    input_text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)