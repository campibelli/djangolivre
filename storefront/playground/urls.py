from django.urls import path
from . import views

#UrlConfiguration Module
urlpatterns = [
    path('hello/',views.say_hello)
]