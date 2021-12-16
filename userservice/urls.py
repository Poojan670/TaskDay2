from django.contrib import admin
from django.urls import path
from .views import  UserList, UserDetail


urlpatterns = [
    path('users/', UserList.as_view(), name= "All the User Details"),
    path('users/<pk>/', UserDetail.as_view(), name="CRUD fuctionality")
]