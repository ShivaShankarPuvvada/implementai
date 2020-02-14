from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.models import User, Group
from rest.models import Rack, Student

from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# from rest_framework.decorators import list_route

from rest.serializers import RackSerializer, StudentSerializer


class RackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows racks to be viewed or edited.
    """
    queryset = Rack.objects.all()
    serializer_class = RackSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_url_kwarg = 'name'

    # def retrieve(self, request, pk=None):
    #     queryset = Student.objects.all()
    #     student = get_object_or_404(queryset, pk=pk)
    #     serializer = StudentSerializer(student)
    #     return Response(serializer.data)

    # @list_route(methods=['get'], url_path='students/(?P<pk>[^/.]+)')
    # def getByName(self, request, name):
    #     serializer_context = {
    #         'request': request,
    #     }
    #     student = get_object_or_404(Student, name=name)
    #     return Response(StudentSerializer(student, context=serializer_context).data, status=status.HTTP_200_OK)
