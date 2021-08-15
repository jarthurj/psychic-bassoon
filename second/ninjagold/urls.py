from django.urls import path, include
from . import views

urlpatterns = [
	path('/index', views.index),
	path('/process_gold/<str:typer>',views.process_gold),

]