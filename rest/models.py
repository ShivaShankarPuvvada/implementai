from django.db import models
# from django.conf import settings
from django.contrib.auth import get_user_model



# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=30)
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
