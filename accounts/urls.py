from django.urls import path
from . import views

urlpatterns = [
    path('registeruser/', views.registerUser, name='registerUser'),
    path('registervendor/', views.registervendor, name='registervendor'),
    

    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('myAccount/',views.myAccount, name='myAccount'),
    path('custDashboard/',views.custDashboard, name='custDashboard'),
    path('vendorDashboard/',views.vendorDashboard, name='vendorDashboard')

]