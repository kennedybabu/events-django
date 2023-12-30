# from rest_framework import routers
from core.user.viewsets import UserViewset 
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.event.viewsets import EventViewSet
from rest_framework_nested import routers
from core.comment.viewsets import CommentViewSet
from core.blog.viewsets import BlogViewSet
router = routers.SimpleRouter()


router.register(r'user', UserViewset, basename='user')


# auth # 
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh' )


# event #
router.register(r'event', EventViewSet, basename='event')

events_router = routers.NestedSimpleRouter(router, r'event', lookup='event')
events_router.register(r'comment', CommentViewSet, basename='comment')

# blog #
router.register(r'blog', BlogViewSet, basename='blog')

urlpatterns = [
    *router.urls,
    *events_router.urls
]