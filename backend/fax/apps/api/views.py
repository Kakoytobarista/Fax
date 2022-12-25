from rest_framework.permissions import AllowAny, IsAuthenticated
from djoser.views import UserViewSet as DjoserUserViewSet

from apps.api.mixin import ChatMixin, MessageMixin
from apps.api.serializers import CreateMessageSerializer, ReadMessageSerializer, CreateMessageSerializer, \
    CustomUserSerializer
from apps.chat.models import Chat, Message
from apps.api.serializers import ChatSerializer, CreateMessageSerializer, ChatSerializer, CustomUserSerializer

from apps.account.models import User


class ChatViewSet(ChatMixin):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)


class MessageViewSet(MessageMixin):
    queryset = Message.objects.all()
    serializer_class = ReadMessageSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return CreateMessageSerializer
        return ReadMessageSerializer


class CustomUserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny, )
