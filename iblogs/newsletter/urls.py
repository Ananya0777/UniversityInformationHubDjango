from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, mail_letter

urlpatterns = [

    path('newsletter/', index),
    path('mail/', mail_letter)

]
