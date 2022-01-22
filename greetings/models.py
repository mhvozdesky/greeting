from django.db import models


class Visitor(models.Model):
    name = models.CharField(max_length=200, default='')
    surname = models.CharField(max_length=200, default='')
