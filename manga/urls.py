from django.urls import path
from . import views

urlpatterns = [
    path('', views.manga, name = "mangaHome"),
]
