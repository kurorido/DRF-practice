from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TagTests(APITestCase):

    def test_create_tag(self):

        url = reverse('blog:tag-list')
        data = {'tag_name': 'Hello_Tag'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)