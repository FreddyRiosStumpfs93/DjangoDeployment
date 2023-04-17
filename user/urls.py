from django.urls import path, include
from rest_framework import routers
from user.views import *

app_name = 'user'
urlpatterns = [

    # vistas basadas en clases

    #USER
    path('list/', UserListView.as_view(), name = 'user_list'),
    path('create/', UserCreateView.as_view(), name = 'user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name = 'user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name = 'user_delete'),

    path('register/', UserCreateView2.as_view(), name='user_register'),

]
