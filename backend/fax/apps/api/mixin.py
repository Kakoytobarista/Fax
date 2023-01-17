from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class BaseMixinViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    """
    Mixin for getting, deleting, creating mixin-viewSet,
    updating of ChatViewSet, MessageViewSet
    """
    queryset = None
    serializer_class = None
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return self.create_serializer_class
        return self.read_serializer_class
