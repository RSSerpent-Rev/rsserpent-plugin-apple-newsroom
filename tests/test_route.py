from starlette.testclient import TestClient


def test_route(client: TestClient) -> None:
    """Test `rsserpent_plugin_apple_newsroom.route`."""
    response = client.get("/apple-newsroom")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/atom+xml;charset=utf-8"
    assert response.text.count("<title>Apple Newsroom</title>") == 1
