# Create your tests here.
import pytest 

from core.fixtures.user import user
from core.event.models import Event 

@pytest.mark.django_db
def test_create_event(user):
    event = Event.objects.create(author=user, body="Test Event Body", date="2023-10-29T18:06:49.883845Z")
    assert event.body == 'Test Event Body'
    assert event.date == '2023-10-29T18:06:49.883845Z'
    assert event.author == user