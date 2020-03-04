from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
# from django.contrib.auth.models import User, Group
from rest.models import Job

from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# from rest_framework.decorators import list_route

from rest.serializers import JobSerializer

from rest.permissions import IsOwnerOrReadOnly

class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows racks to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
