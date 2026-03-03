from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "AnimeHome"),
    # path('about/', views.about, name = "AboutUs"),
    # path('contact/', views.contact, name = "Contact"),
    # path('tracker/', views.tracker, name = "trackingStatus"),
    # path('search/', views.search, name = "search"),
    path('product/', views.product, name = "product"),
    path('demo/', views.demo, name = "demo"),
]
