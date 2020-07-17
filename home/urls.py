from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.registerUser),
    path('authenticate', views.login),
    path('success', views.success),
    path('logout', views.logout)
    
]
