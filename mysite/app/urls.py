from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('profile/', views.profile, name='profile'),
]