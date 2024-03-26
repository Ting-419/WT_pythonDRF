from django.urls import path

from blog.views import PostList, PostUpdate

urlpatterns = [
    path('<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('', PostList.as_view(), name='post_list'),
]
