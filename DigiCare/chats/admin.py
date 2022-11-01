from django.contrib import admin

from chats.models import Chat, Feedback

# Register your models here.
admin.site.register(Chat)
admin.site.register(Feedback)