from django.contrib.auth.models import User
from rest.models import Job
from rest_framework import serializers




class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Job
        fields = ['id', 'title', 'posted_by', 'description', 'skills', 'experience_from', 'experience_to', 'educational_qualification', 'certifications', 'languages', 'notice_period_in_days', 'job_type', 'location']

    


