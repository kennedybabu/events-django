from rest_framework import routers
from core.user.viewsets import UserViewset 
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet


router = routers.SimpleRouter()


router.register(r'user', UserViewset, basename='user')


# auth # 
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh' )

urlpatterns = [
    *router.urls,
]