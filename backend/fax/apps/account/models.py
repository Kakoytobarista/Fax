import django.contrib.auth.validators
from django.contrib.auth.models import AbstractUser
from django.db import models, transaction
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from apps.chat.models import Chat, Message


class User(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
        verbose_name='Username of the user',
    )
    email = models.EmailField(
        max_length=50,
        verbose_name='Email of the user',
        blank=True,
    )
    first_name = models.CharField(
        blank=True,
        max_length=50,
        verbose_name='Name of the user',
    )
    surname = models.CharField(
        blank=True,
        max_length=50,
        verbose_name='Surname of the user',
    )
    is_online = models.BooleanField(default=False,
                                    verbose_name='Online status'
                                    )
    friends = models.ManyToManyField('self',
                                     symmetrical=False,
                                     related_name='user_friends',
                                     blank=True
                                     )

    def __str__(self):
        return f"PK: {self.pk} - {str(self.username).capitalize()}"

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


@receiver(models.signals.pre_delete, sender=User)
def delete_user_related_objects(instance, **kwargs):
    with transaction.atomic():
        messages = Message.objects.filter(author=instance)
        messages.delete()
        chat = get_object_or_404(Chat, participants=instance)
        chat.delete()
