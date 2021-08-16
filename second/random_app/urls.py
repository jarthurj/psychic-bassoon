from django.urls import path
from random_app import views
urlpatterns = [
	path('', views.index),
	path('reset', views.reset)

]