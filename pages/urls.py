from django.urls import path, re_path
from pages import views

urlpatterns = [re_path(r"^$", views.index)]
