from django.db import models

from fax.settings import AUTH_USER_MODEL


class Message(models.Model):
    author = models.ForeignKey(
        AUTH_USER_MODEL, related_name='message_author', on_delete=models.CASCADE,
        verbose_name='Author_of_message'
    )
    content = models.TextField(verbose_name='Text of message')
    created = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Created time'
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pk} - {self.content} - {self.created}'


class Chat(models.Model):
    participants = models.ManyToManyField(
        AUTH_USER_MODEL, related_name='chat_participants',
        blank=True,
        verbose_name='Participants of chat',
    )
    messages = models.ManyToManyField(
        Message, blank=True, verbose_name='Messages of chat'
    )

    def __str__(self):
        return f'Chat: {self.pk} - Participants: {self.participants}'
