from rest_framework import mixins
from rest_framework import viewsets


class ChatMixin(mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):
    """
    Mixin for getting, deleting, creating mixin-viewSet,
    updating of ChatViewSet
    """
    pass


class MessageMixin(mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    """
    Mixin for getting, deleting, creating mixin-viewSet,
    updating of MessageViewSet
    """
    pass
