from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class MyCaps(models.Model):
    name = models.CharField(max_length=45)
    color = models.ForeignKey(Color)

    def __str__(self):
        return self.name