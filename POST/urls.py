from django.contrib import admin
from django.urls import path
from . import views
from .views import PostList, PostDetail


urlpatterns = [
    path('posts/', PostList.as_view(), name= "All the User Details"),
    path('posts/<pk>/', PostDetail.as_view(), name="CRUD fuctionality")
]