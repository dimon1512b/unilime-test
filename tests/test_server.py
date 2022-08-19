from starlette import status


def test_main_url(client) -> None:
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK, "Status must be 200"
