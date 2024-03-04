from rest_framework.viewsets import ModelViewSet

from apps.posts.models import Post
from apps.posts.api.serializers import PostSerializer


class PostApiViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer