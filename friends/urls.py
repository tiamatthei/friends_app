from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /friends
    path('friends', views.friends, name='friends'),
    # ex: /user
    path('user', views.user, name='user'),
    # ex: /register
    path('register', views.register, name='register'),
]