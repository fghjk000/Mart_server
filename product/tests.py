from django.test import TestCase

from product.models import Product


class ProductViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(name="새우깡", price=1000, category="과자")

    def test_목록조회(self):
        response = self.client.get("/product/")
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["id"], self.product.id)
        self.assertEqual(response_data[0]["name"], self.product.name)
        self.assertEqual(response_data[0]["price"], self.product.price)
        self.assertEqual(response_data[0]["category"], self.product.category)

    def test_단건조회(self):
        response = self.client.get(f"/product/{self.product.id}/")
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 4)
