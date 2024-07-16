from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class OrderPageTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('order_page')
        self.valid_payload = {
            "id": "A0000000",
            "name": "Kevin",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
                },
            "price": 1000,
            "currency": "TWD"
        }
        self.invalid_name_english_payload = {
            "id": "A0000000",
            "name": "K中文",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 1000,
            "currency": "TWD"
        }
        self.invalid_name_capitalized_payload = {
            "id": "A0000000",
            "name": "kevin",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 1000,
            "currency": "TWD"
        }
        self.invalid_currency_payload = {
            "id": "A0000000",
            "name": "Kevin",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 1000,
            "currency": "EUR"
        }
        self.price_over_2000_payload = {
            "id": "A0000000",
            "name": "Kevin",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 3000,
            "currency": "TWD"
        }
        self.usd_currency_payload = {
            "id": "A0000000",
            "name": "Kevin",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 70,
            "currency": "USD"
        }
        self.invalid_address_city_payload = {
            "id": "A0000000",
            "name": "Kevin",
            "address": {
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 1000,
            "currency": "TWD"
        }
        self.invalid_address_district_payload = {
            "id": "A0000000",
            "name": "Kevin",
            "address": {
                "city": "taipei-city",
                "street": "fuxing-south-road"
            },
            "price": 1000,
            "currency": "TWD"
        }
        self.invalid_address_street_payload = {
            "id": "A0000000",
            "name": "Kevin",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district"
            },
            "price": 1000,
            "currency": "TWD"
        }
    def test_valid_payload(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("PASS", response.content.decode())

    def test_invalid_name_english_payload(self):
        response = self.client.post(self.url, self.invalid_name_english_payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Name contains non-English characters", response.content.decode())

    def test_invalid_name_capitalized_payload(self):
        response = self.client.post(self.url, self.invalid_name_capitalized_payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Name is not capitalized", response.content.decode())

    def test_invalid_currency_payload(self):
        response = self.client.post(self.url, self.invalid_currency_payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Currency format is wrong", response.content.decode())

    def test_price_over_2000_payload(self):
        response = self.client.post(self.url, self.price_over_2000_payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Price is over 2000", response.content.decode())

    def test_usd_currency_payload(self):
        response = self.client.post(self.url, self.usd_currency_payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Price is over 2000", response.content.decode())

    def test_invalid_address_city_payload(self):
        response = self.client.post(self.url, self.invalid_address_city_payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please check form 'city' is complete.", response.content.decode())

    def test_invalid_address_district_payload(self):
        response = self.client.post(self.url, self.invalid_address_district_payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please check form 'district' is complete.", response.content.decode())

    def test_invalid_address_street_payload(self):
        response = self.client.post(self.url, self.invalid_address_street_payload, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Please check form 'street' is complete.", response.content.decode())

