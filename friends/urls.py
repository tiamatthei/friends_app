from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /friends
    path('friends', views.friends, name='friends'),
    # ex: /add_friend
    path('add_friend', views.add_friend, name='add_friend'),
    # ex: /remove_friend
    path('remove_friend', views.remove_friend, name='remove_friend'),
    # ex: /user
    path('user', views.user, name='user'),
    # ex: /register
    path('register', views.register, name='register'),
    # ex: /login
    path('login', views.login, name='login'),
]