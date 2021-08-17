from django.urls import path, include
from . import views

urlpatterns = [
	path('register', views.index),
	path('login', views.login),
	path('users/new', views.index),
	path('users', views.users),
	path('', views.blogs)
]