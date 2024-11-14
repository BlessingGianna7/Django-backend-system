from django.db import models

class Guider(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    service_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.name
