from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/DrawRating', views.draw_rating),
]
