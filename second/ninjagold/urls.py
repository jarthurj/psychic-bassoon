from django.urls import path, include
from ninjagold import views

urlpatterns = [
	path('', views.index),
	path('process_gold/<str:typer>',views.process_gold),

]