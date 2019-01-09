from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class SearchApiTests(APITestCase):
  def test_invalid_request(self):
    url = reverse('search')
    res = self.client.get(url)
    self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

  def test_valid_request(self):
    url = reverse('search')
    res = self.client.get(f'{url}?q=test')
    self.assertEqual(res.status_code, status.HTTP_200_OK)

  def test_count_param(self):
    url = reverse('search')
    count = 15
    res = self.client.get(f'{url}?q=test&count={count}')
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertTrue(len(res.json()['statuses']) <= count)

