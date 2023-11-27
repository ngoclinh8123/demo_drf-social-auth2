from rest_framework.serializers import ModelSerializer
from module.post.models import Post


class PostSr(ModelSerializer):
    class Meta:
        model = Post
        exclude = ()
