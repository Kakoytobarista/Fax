from django.urls import include, path
from rest_framework import routers

from apps.api.views import MessageViewSet, CustomUserViewSet, ChatViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('message', MessageViewSet, basename='message')
router.register('chat', ChatViewSet, basename='chat')
router.register('users', CustomUserViewSet, basename='users')


urlpatterns = (
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
)
