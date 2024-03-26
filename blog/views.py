from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post
from blog.serializers import PostSerializer


class PostList(APIView):
    def get(self, request, format=None):
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)
