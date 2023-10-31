from rest_framework import routers
from core.user.viewsets import UserViewset 
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.event.viewsets import EventViewSet

router = routers.SimpleRouter()


router.register(r'user', UserViewset, basename='user')


# auth # 
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh' )


# post #
router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    *router.urls,
]