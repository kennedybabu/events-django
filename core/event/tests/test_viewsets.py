from rest_framework import status 

from core.fixtures.user import user 
from core.fixtures.event import event 

class TestEventViewSet:
    endpoint = '/api/event/'

    def test_list(self, client, user, event):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve(self, client, user, event):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(event.public_id) + "/")
        assert response.status_code == status.HTTP_200_OK 
        assert response.data['id'] == event.public_id.hex 
        assert response.data['body'] == event.body 
        assert response.data['date'] == event.date 
        assert response.data['author']['id'] == event.author.public_id.hex

    def test_create(self, client, user):
        client.force_authenticate(user=user)
        data = {
            "body": "Test Event Body",
            "date": "2023-10-29T18:06:49.883871Z",
            "author": user.public_id.hex
        }

        response = client.event(self.endpoint, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['body'] == data['body']
        assert response.data['date'] == data['date']
        assert response.data['author']['id'] == user.public_id.hex 

    def test_update(self, client, user, event):
        client.force_authenticate(user=user)
        data = {
            "body": "Test Event Body",
            "date": "2023-10-29T18:06:49.883871Z",
            "author": user.public_id.hex
        }

        response = client.put(self.endpoint + str(event.public_id) + "/", data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['body'] == data['body']

    def test_delete(self, client, user, event):
        client.force_authenticate(user=user)
        response = client.delete(self.endpoint + str(event.public_id) + "/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1 

    def test_retrieve_anonymous(self, client, event):
        response = client.get(self.endpoint + str(event.public_id) + "/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == event.public_id.hex 
        assert response.data['body'] == event.body
        assert response.data['author']['id'] == event.author.public_id.hex
