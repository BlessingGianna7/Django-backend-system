from django.db import models
from guiders.models import Guider

class Guest(models.Model):
    name = models.CharField(max_length=100)
    visit_date = models.DateField()
    guiders = models.ManyToManyField('guiders.Guider', related_name='guests')


    def __str__(self):
        return self.name
