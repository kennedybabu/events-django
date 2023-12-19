# Create your tests here.
import pytest 
from rest_framework import status 
from core.fixtures.user import user 
# from core.fixtures.event import event

class TestAuthenticationViewSet:
    endpoint = "/api/auth/"


    def test_login(self, client, user):        
        data = {
            "email": user.email,
            "password": "test_password"
        }

        response = client.post(self.endpoint + "login/", data)

        assert response.status_code == status.HTTP_200_OK 
        assert response.data['access']
        assert response.data['user']['id'] == user.public_id.hex 
        assert response.data['user']['username'] == user.username 
        assert response.data['user']['email'] == user.email

    @pytest.mark.django_db 
    def test_register(self, client):
        data = {
            "username": "johndoe",
            "email": "johndoe@mail.com",
            "password": "test_password",
            "first_name": "John",
            "last_name": "Doe"          
        }

        response = client.post(self.endpoint + "register/", data)

        assert response.status_code == status.HTTP_201_CREATED

    def test_refresh(self, client, user):
        data = {
            "email": user.email,
            "password": "test_password"
        }

        response = client.post(self.endpoint + "login/", data)
        assert response.status_code == status.HTTP_200_OK

        data_refresh = {
            "refresh": response.data['refresh']
        }
        response = client.post(self.endpoint + "refresh/", data_refresh)
        assert response.status_code == status.HTTP_200_OK 
        assert response.data['access']

    # def test_create_anonymous(self, client):
    #     data = {
    #         "body": "Test Event Body",
    #         "date": "2023-10-29T18:06:49.883871Z",
    #         "author": "test_user"
    #     }
    #     response = client.post(self.endpoint, data)
    #     assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # def test_update_anonymous(self, client, event):
    #     data = {
    #         "body": "Test Event body",
    #         "date": "2023-10-29T18:06:49.883871Z",
    #         "author": "test_user"
    #     }

    #     response = client.put(self.endpoint + str(event.public_id) + "/", data)
    #     assert response.status_code == status.HTTP_401_UNAUTHORIZED

