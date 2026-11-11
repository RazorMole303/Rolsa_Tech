from django.test import TestCase
from django.urls import reverse


class StorePageTests(TestCase):
    def test_store_page_renders_with_products(self):
        response = self.client.get(reverse('store'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Solar Panels')
        self.assertContains(response, 'Electric Cars')
        self.assertContains(response, 'Wind Farms')

    def test_store_purchase_submits_successfully(self):
        response = self.client.post(
            reverse('store'),
            {
                'product': 'solar-panels',
                'quantity': 2,
                'full_name': 'Alice Smith',
                'email': 'alice@example.com',
                'location': 'Cape Town',
                'notes': 'Need installation support.',
            },
            follow=True,
        )

        self.assertRedirects(response, reverse('store'))
        self.assertContains(response, 'Your order for Solar Panels has been received.')
