from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes, name='classes'),
    path('add/', views.add_classes, name='add_classes'),
]
