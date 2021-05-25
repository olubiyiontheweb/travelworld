from typing import KeysView
from django.urls import path, re_path
from hotels import views

urlpatterns = [path("", views.index)]
