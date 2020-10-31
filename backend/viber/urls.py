from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('getPlaylist/<int:id>/', views.getPlaylist, name='getPlaylist'),
    path('getSong/<int:id>/', views.getSong, name='getSong')
]