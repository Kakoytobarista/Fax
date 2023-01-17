from rest_framework.permissions import AllowAny, IsAuthenticated
from djoser.views import UserViewSet as DjoserUserViewSet

from apps.api.mixin import BaseMixinViewSet
from apps.api.serializers import CreateMessageSerializer, ReadMessageSerializer, CreateMessageSerializer, \
    CustomUserSerializer, ReadChatSerializer, CreateChatSerializer
from apps.chat.models import Chat, Message
from apps.api.serializers import ReadChatSerializer, CreateMessageSerializer, \
    CreateChatSerializer, CustomUserSerializer

from apps.account.models import User


class ChatViewSet(BaseMixinViewSet):
    queryset = Chat.objects.all()
    read_serializer_class = ReadChatSerializer
    create_serializer_class = CreateChatSerializer

    def perform_create(self, serializer):
        serializer.save(chat_owner=self.request.user)


class MessageViewSet(BaseMixinViewSet):
    queryset = Message.objects.all()
    read_serializer_class = ReadMessageSerializer
    create_serializer_class = CreateMessageSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CustomUserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny, )
