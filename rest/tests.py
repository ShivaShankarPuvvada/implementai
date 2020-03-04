from django.test import TestCase
from rest.models import Job

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate


from django.contrib.auth.models import User


factory = APIRequestFactory()


request = factory.get('/jobs/')


user = User.objects.get(username='testuser')
view = AccountDetail.as_view()



request1 = factory.post('/jobs/', {'title': 'Full stack developer'})
force_authenticate(request1, user=user, token=user.auth_token)
response = view(request1)


request2 = factory.put('/jobs/1/', {'title': 'Angular 1 js developer'})
force_authenticate(request2, user=user, token=user.auth_token)
response = view(request2)


request3 = factory.delete('/jobs/1/')
force_authenticate(request3, user=user, token=user.auth_token)
response = view(request3)



