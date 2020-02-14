# from django.contrib.auth.models import User, Group
from rest.models import Rack, Student
from rest_framework import serializers



class RackSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.SlugRelatedField(many=True, queryset=Student.objects.all(), slug_field='name') # comment this line if hyperlinks are needed
    class Meta:
        model = Rack
        fields = ['id', 'title', 'students']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    rack = serializers.SlugRelatedField(many=True, queryset=Rack.objects.all(), slug_field='title') # comment this line if hyperlinks are needed
    class Meta:
        model = Student
        fields = ['id', 'name', 'rack']