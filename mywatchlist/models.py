from django.db import models

class MyWatchList(models.Model):
    title = models.CharField(max_length=255)