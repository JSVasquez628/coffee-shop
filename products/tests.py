from django.test import TestCase
from django.urls import reverse

class ProductListViewTest(TestCase):
    def test_should_retourn_200(self):
        url = reverse('list_products')
        response = self.client.get(url)
        breakpoint()
        self.assertEqual(response.status_code, 200)
