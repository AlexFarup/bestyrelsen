from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('members/', views.members),
    path('events/', views.events),
    path('leaderboard/', views.leaderboard),
    path('login/', views.login),
    path('register/', views.register)
]
