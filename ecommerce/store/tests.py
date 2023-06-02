from django.test import TestCase
from . models import Customer

class ModelTest(TestCase):

    def setUp(self):
        self.store = Customer.objects.create(name="ivan", email="name@gmail.com")

    def test_post_model(self):
        d = self.store
        self.assertTrue(isinstance(d, Customer))
