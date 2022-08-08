"""
Tests for hello API.
"""
HELLO_URL = '/hello'


def test_get_hello(client):
    """Test for hello api get request."""
    res = client.get(HELLO_URL)

    assert res.status_code == 200


def test_get_hello_with_typo_in_url(client):
    """Test response 404 when typo in hello request url."""
    res = client.get('/hello/')

    assert res.status_code == 404
