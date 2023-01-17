from django.contrib import admin

from apps.chat.models import Chat, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created')
    list_display_links = ('author',)
    list_editable = ('content', )


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('get_messages_list', 'chat_owner', 'recipient', )
    filter_horizontal = ('messages', )

    @staticmethod
    def get_messages_list(obj):
        return ", ".join([str(item) for item in obj.messages.all()])
