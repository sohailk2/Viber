from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('getPlaylist/<str:id>/', views.getPlaylist, name='getPlaylist'),
    path('getSong/<str:id>/', views.getSong, name='getSong'),
    path('getSearches/<str:id>/', views.getSearches, name='getSearches'),
    path('getFriends/<str:id>/', views.getFriends, name='getFriends'),
    path('delFriend/', views.delFriend, name='delFriend'),
    path('addFriend/', views.addFriend, name='addFriend')


]