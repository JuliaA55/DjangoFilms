from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:id>/', views.movie_detail, name='movie_detail'),
    path('create/', views.movie_create, name='movie_create'),
]