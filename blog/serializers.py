from rest_framework import serializers

from blog.models import Post, Comment, Phone


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'user', 'text')


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('id', 'post', 'user', 'phone_number')






