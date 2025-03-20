from django.db import models

class Timer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    segment = models.CharField(max_length=3)

    def __str__(self):
        return self.name