from django.db import models

# Create your models here.
class Rack(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    rack = models.ManyToManyField('Rack', blank=True, related_name='students')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name