from django.urls import path
from . import views
urlpatterns = [
	path('', views.index),
	path('new', views.new),
	path('create', views.create),
	path('<int:blog_number>', views.show),
	path('<int:blog_number>/edit', views.edit),
	path('<int:blog_number>/delete', views.destroy),
]