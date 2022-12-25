from rest_framework import serializers

from apps.chat.models import Chat, Message
from apps.account.models import User


class ReadMessageSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ('author',
                  'content',
                  'created',)


class CreateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('content',
                  'created')


class ChatSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField()
    messages = serializers.StringRelatedField()

    class Meta:
        model = Chat
        fields = ('participants',
                  'messages',
                  )


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            'username',
            'password',
        )
