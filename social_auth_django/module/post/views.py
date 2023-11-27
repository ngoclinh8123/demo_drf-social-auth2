from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post
from .helper.sr import PostSr


class PostView(GenericViewSet):
    serializer_class = PostSr
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        print(request.user)
        qs = super().get_queryset().order_by("-id")
        posts = Post.objects.all().order_by("-id")
        serializer = PostSr(qs, many=True)
        return Response(serializer.data)

    def add(self, request):
        print(request.user)
        serializer = PostSr(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        post_serializer = PostSr(post)
        return Response(post_serializer.data)
