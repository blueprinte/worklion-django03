from django.urls import path
from . import views

app_name="post"

urlpatterns = [
	path('new/', views.new, name='new'),
	path('lists/', views.lists, name='lists'),
]