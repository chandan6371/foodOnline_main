from django.urls import path
from . import views

urlpatterns = [
    path('registeruser/', views.registerUser, name='registerUser'),
    path('registervendor/', views.registervendor, name='registervendor'),
]