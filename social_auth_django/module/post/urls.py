import os
from django.urls import path
from .views import PostView

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("", PostView.as_view({"get": "list", "post": "add"})),
]
