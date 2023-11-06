import pytest 


from core.fixtures.user import user 
from core.event.models import Event 


@pytest.fixture
def event(db, user):
    return Event.objects.create(author=user, body="Test Event Body", date="2023-10-29T18:06:49.883845Z")