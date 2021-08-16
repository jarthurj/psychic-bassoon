from django.urls import path, include
from ninjagold import views

urlpatterns = [
	path('', views.index, name="home_gold"),
	path('process_gold/<str:typer>',views.process_gold, name="get_gold"),

]