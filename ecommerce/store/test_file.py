import pytest
from django.urls import reverse
import pytest
from .models import Customer


@pytest.mark.django_db
def test_customer_create():

    customer = Customer.objects.create(name="Igor", email="igor@gmail.com")

    assert customer.name == "Igor"
    assert customer.email == "igor@gmail.com"

