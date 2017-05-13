from __future__ import unicode_literals

from django.db import models


class Template(models.Model):
    CHOICES = (
        ('pu', 'Public'),
        ('pr', 'Private'),
    )
    name = models.CharField(max_length=64)
    description = models.TextField()
    privacy = models.CharField(max_length=2, choices=CHOICES, default='pu')

    def __str__(self):
        return self.name
