from django.urls import path
from .views import UserList, UserUpdate


urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserUpdate.as_view(), name='user-update'),
]


