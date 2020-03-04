from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from rest.models import Job
from rest.views import JobViewSet

from rest.serializers import JobSerializer

from rest_framework.test import APIRequestFactory




class CreateJobTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('testuser', 'testuser@gmail.com', 'testpassword')

        self.client.login(username='testuser', password='testpassword')
        self.data = {'title':'test job one', 'posted_by':self.superuser, 'description':'test job one description', 'skills':'node js, oracle', 'experience_from':'10', 'experience_to':'15', 'educational_qualification':'B.Tech', 'certifications':'OCJP', 'languages':'English', 'notice_period_in_days':'120', 'job_type':'PE', 'location':'Hyderabad'}


    def test_can_create_job(self):
        response = self.client.post(reverse('job-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadJobTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('testuser', 'testuser@gmail.com', 'testpassword')

        self.client.login(username='testuser', password='testpassword')
        self.job = Job.objects.create(title="update title", posted_by=self.superuser, description='update desc', skills='java, python', experience_from='03', experience_to='04', educational_qualification='B.Tech', certifications='OCJP', languages='Telugu', notice_period_in_days='54', location='hyderabad')


    def test_can_read_job_list(self):
        response = self.client.get(reverse('job-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_job_detail(self):
        response = self.client.get(reverse('job-detail', args=[self.job.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateJobTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('testuser', 'testuser@gmail.com', 'testpassword')

        self.client.login(username='testuser', password='testpassword')


        self.job = Job.objects.create(title="update title", posted_by=self.superuser, description='update desc', skills='java, python', experience_from='03', experience_to='04', educational_qualification='B.Tech', certifications='OCJP', languages='Telugu', notice_period_in_days='54', location='hyderabad')

        self.data = JobSerializer(self.job).data
        self.data.update({'title': 'Changed title'})

    def test_can_update_job(self):
        response = self.client.put(reverse('job-detail', args=[self.job.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteJobTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('testuser', 'testuser@gmail.com', 'testpassword')

        self.client.login(username='testuser', password='testpassword')

        self.job = Job.objects.create(title="delete title", posted_by=self.superuser, description='delete desc', skills='java, c', experience_from='03', experience_to='04', educational_qualification='B.Tech', certifications='OCJP', languages='Telugu', notice_period_in_days='54', location='hyderabad')

    def test_can_delete_user(self):
        response = self.client.delete(reverse('job-detail', args=[self.job.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)