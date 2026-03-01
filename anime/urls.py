from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime, name = "AnimeHome"),
    # path('about/', views.about, name = "AboutUs"),
    # path('contact/', views.contact, name = "Contact"),
    # path('tracker/', views.tracker, name = "trackingStatus"),
    # path('search/', views.search, name = "search"),
    path('product/', views.product, name = "product"),
    # path('checkout/', views.checkout, name = "checkout"),
]
