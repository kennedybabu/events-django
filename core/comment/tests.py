# Create your tests here.
import pytest 

from core.fixtures.user import user 
from core.fixtures.event import event 
from core.comment.models import Comment 

@pytest.mark.django_db 
def test_create_comment(user, event):
    comment = Comment.objects.create(author=user, event=event, body="Test comment body")
    assert comment.author == user 
    assert comment.event == event 
    assert comment.body == "Test comment body"
