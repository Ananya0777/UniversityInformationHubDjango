from django.contrib import admin
from . models import Subscribers, MailMessage

# register models here

admin.site.register(MailMessage)
admin.site.register(Subscribers)

