from django.urls import path

from blog.views import PostList, PostUpdate
from custom_user.views import UserList, UserUpdate

urlpatterns = [
    path('<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('', PostList.as_view(), name='post_list'),
    path('', UserList.as_view(), name='user_list'),
]

from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CommentViewSet, PhoneViewSet
router = DefaultRouter()
router.register(r'blog', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'phone', PhoneViewSet)
urlpatterns += router.urls
