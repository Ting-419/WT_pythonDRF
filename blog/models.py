from django.db import models

from custom_user.models import User
# from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    text = models.TextField()


class Phone(models.Model):
    post = models.ForeignKey(Post, related_name='phone', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_phone')
    phone_number = models.CharField(max_length=20)


