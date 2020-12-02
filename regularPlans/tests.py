from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


# Create your tests here.

class TestSetUp(APITestCase):
    def setUp(self):
        self.regular_plan_url = reverse("regular-plans/")
        self.owner_url = reverse("owners/")

        return super().setUp()


class TestViews(TestSetUp):
    def test_can_register_owner(self):
        owner_data = {
            "id": 1,
            "name": "Owner teste",
            "email": "teste3@teste.com",
            "password": "teste"
        }
        res = self.client.post(self.owner_url, owner_data, format="json")
        self.assertEqual(res.status_code, 201)

    def test_cannot_create_regular_plan_with_wrong_vet(self):
        regular_plan_data = {
            "name": "Owner teste 2",
            "tar_included": True,
            "subscription": 10.0,
            "cycle": "D",
            "type": "TS",
            "offer_iva": True,
            "off_peak_price": 10.0,
            "peak_price": 12.0,
            "unit": "KH",
            "valid": True,
            "publish": False,
            "vat": 0,
            "owner": 1
        }
        res = self.client.post(self.regular_plan_url, regular_plan_data, format="json")
        self.assertEqual(res.status_code, 400)

    def test_can_create_regular_plan_with_correct_vet(self):
        regular_plan_data = {
            "name": "Owner teste 2",
            "tar_included": True,
            "subscription": 10.0,
            "cycle": "D",
            "type": "TS",
            "offer_iva": True,
            "off_peak_price": 10.0,
            "peak_price": 12.0,
            "unit": "KH",
            "valid": True,
            "publish": False,
            "vat": 1,
            "owner": 1
        }
        res = self.client.post(self.regular_plan_url, regular_plan_data, format="json")
        self.assertEqual(res.status_code, 201)

    def test_cannot_create_regular_plan_with_owner_null(self):
        regular_plan_data = {
            "name": "Owner teste 2",
            "tar_included": True,
            "subscription": 10.0,
            "cycle": "D",
            "type": "TS",
            "offer_iva": True,
            "off_peak_price": 10.0,
            "peak_price": 12.0,
            "unit": "KH",
            "valid": True,
            "publish": False,
            "vat": 1,
            "owner": None
        }
        res = self.client.post(self.regular_plan_url, regular_plan_data, format="json")
        self.assertEqual(res.status_code, 400)

    def test_can_create_regular_plan_with_owner_null(self):
        regular_plan_data = {
            "name": "Owner teste 2",
            "tar_included": True,
            "subscription": 10.0,
            "cycle": "D",
            "type": "TS",
            "offer_iva": True,
            "off_peak_price": 10.0,
            "peak_price": 12.0,
            "unit": "KH",
            "valid": True,
            "publish": True,
            "vat": 1,
            "owner": None
        }
        res = self.client.post(self.regular_plan_url, regular_plan_data, format="json")
        self.assertEqual(res.status_code, 201)

    def test_cannot_create_regular_plan_with_wrong_cycle(self):
        regular_plan_data = {
            "name": "Owner teste 2",
            "tar_included": True,
            "subscription": 10.0,
            "cycle": "F",
            "type": "TS",
            "offer_iva": True,
            "off_peak_price": 10.0,
            "peak_price": 12.0,
            "unit": "KH",
            "valid": True,
            "publish": True,
            "vat": 1,
            "owner": None
        }
        res = self.client.post(self.regular_plan_url, regular_plan_data, format="json")
        self.assertEqual(res.status_code, 400)

    def test_can_create_regular_plan_with_correct_cycle(self):
        regular_plan_data = {
            "name": "Owner teste 2",
            "tar_included": True,
            "subscription": 10.0,
            "cycle": "W",
            "type": "TS",
            "offer_iva": True,
            "off_peak_price": 10.0,
            "peak_price": 12.0,
            "unit": "KH",
            "valid": True,
            "publish": True,
            "vat": 1,
            "owner": None
        }
        res = self.client.post(self.regular_plan_url, regular_plan_data, format="json")
        self.assertEqual(res.status_code, 400)
