from django.db import models

from fax.settings import AUTH_USER_MODEL


class Message(models.Model):
    author = models.ForeignKey(
        AUTH_USER_MODEL, related_name='message_author',
        on_delete=models.CASCADE, verbose_name='Author_of_message'
    )
    content = models.TextField(verbose_name='Text of message')
    created = models.DateTimeField(
        auto_now_add=True, db_index=True,
        verbose_name='Created time'
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pk} - {self.content} - {self.created}'


class Chat(models.Model):
    recipient = models.ForeignKey(
        AUTH_USER_MODEL, related_name='chat_recipient',
        on_delete=models.CASCADE, verbose_name='Chat recipient'
    )
    chat_owner = models.ForeignKey(
        AUTH_USER_MODEL, related_name='chat_owner',
        on_delete=models.CASCADE, verbose_name='Chat owner'
    )
    messages = models.ManyToManyField(
        Message, related_name='chat_messages',
        blank=True, verbose_name='Messages of chat'
    )

    def __str__(self):
        return (f'Chat: {self.pk} - Chat owner: {self.chat_owner} '
                f'- Chat recipient: {self.recipient}')
