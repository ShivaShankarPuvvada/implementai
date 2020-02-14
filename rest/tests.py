from django.test import TestCase
from rest.models import Rack, Student

from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()


request = factory.post('/racks/', {'title': 'R33'})
request = factory.put('/racks/12/', {'title': 'R11'})


request = factory.post('/students/', {'name': 'S6'})

# testing manytomanyfield
racks = ['R1', 'R2', 'R3']
request = factory.put('/students/4/', {'name': 'S10', 'rack': racks})

