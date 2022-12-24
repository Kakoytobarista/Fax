from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.account.models import User
from apps.chat.models import Chat, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created')
    list_display_links = ('author',)
    list_editable = ('content', )


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('get_participants_list', )
    filter_horizontal = ('participants', 'messages')

    @staticmethod
    def get_participants_list(obj):
        return ", ".join([str(item) for item in obj.participants.all()])


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('friends',)
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Additional info', {
            'fields': ('friends', 'is_online',)
        })
    )

    @staticmethod
    def get_participants_list(obj):
        return ", ".join([str(item) for item in obj.friends.all()])

