from rest_framework import routers
from core.user.viewsets import UserViewset 

router = routers.SimpleRouter()


router.register(r'user', UserViewset, basename='user')

urlpatterns = [
    *router.urls,
]