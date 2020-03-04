from django.db import models
# from django.conf import settings
from django.contrib.auth import get_user_model



# Create your models here.


class Job(models.Model):

    PERMANENT = 'PE'
    CONTRACT = 'CO'
    JOB_TYPE_CHOICES = [
        (PERMANENT, 'Permanent'),
        (CONTRACT, 'Contract'),
    ]

    title = models.CharField(max_length=255)
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=244, blank=True, null=True)
    experience_from = models.CharField(max_length=2, default='00')
    experience_to = models.CharField(max_length=2, default='00')
    educational_qualification = models.CharField(max_length=25, blank=True, null=True)
    certifications = models.CharField(max_length=255, blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)
    notice_period_in_days = models.CharField(max_length=3, default='0')
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES, default=PERMANENT)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateField(auto_now = True)


    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


