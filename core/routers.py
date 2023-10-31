from rest_framework import routers
from core.user.viewsets import UserViewset 
from core.auth.viewsets import RegisterViewSet

router = routers.SimpleRouter()


router.register(r'user', UserViewset, basename='user')


# auth # 
router.register(r'auth/register', RegisterViewSet, basename='auth-register')

urlpatterns = [
    *router.urls,
]