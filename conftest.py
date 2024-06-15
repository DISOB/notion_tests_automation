import pytest

from client.client import Client


@pytest.fixture(scope="session")
def client(request):
    return Client
