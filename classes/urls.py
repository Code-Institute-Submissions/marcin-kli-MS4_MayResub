from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes, name='classes'),
    path('add/', views.add_class, name='add_class'),
    path('edit/<int:classes_id>/', views.edit_class, name='edit_class'),
]
