from django.contrib import admin

from apps.account.models import User


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
