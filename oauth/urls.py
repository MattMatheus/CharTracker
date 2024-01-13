from django.urls import path
from . import views
from . import oauth

urlpatterns = [
    path("login", oauth.process_login, name="login"),
    path("callback", oauth.callback, name="callback"),
]
