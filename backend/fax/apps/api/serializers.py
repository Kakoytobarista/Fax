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


class ReadChatSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)
    messages = serializers.StringRelatedField(many=True)

    class Meta:
        model = Chat
        fields = (
            'id',
            'participants',
            'messages',
            'chat_owner',
                  )


class CreateChatSerializer(serializers.ModelSerializer):
    chat_owner = serializers.StringRelatedField()

    class Meta:
        model = Chat
        fields = (
            'id',
            'participants',
            'messages',
            'chat_owner'
                  )

    @staticmethod
    def validate_participants(value):
        if not value:
            raise serializers.ValidationError(
                'You need to add least one member.'
            )
        return value


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            'username',
            'password',
        )
