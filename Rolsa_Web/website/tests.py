from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import StorePurchase


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

    def test_store_purchase_saves_logged_in_user_and_form_data(self):
        user = get_user_model().objects.create_user(
            username='alicesmith',
            email='alice@example.com',
            password='SecurePass123!',
        )
        self.client.force_login(user)

        self.client.post(
            reverse('store'),
            {
                'product': 'electric-cars',
                'quantity': 1,
                'full_name': 'Alice Smith',
                'email': 'alice@example.com',
                'location': 'Johannesburg',
                'notes': 'Please contact me about delivery.',
            },
            follow=True,
        )

        purchase = StorePurchase.objects.get(user=user)
        self.assertEqual(purchase.product, 'electric-cars')
        self.assertEqual(purchase.quantity, 1)
        self.assertEqual(purchase.full_name, 'Alice Smith')
        self.assertEqual(purchase.email, 'alice@example.com')
        self.assertEqual(purchase.location, 'Johannesburg')
        self.assertEqual(purchase.notes, 'Please contact me about delivery.')
