from django.contrib.auth.models import User
from blog.serializers import UserSerializer, ArticleSerializer, TagSerializer
from rest_framework import viewsets
from blog.models import Article, Tag

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

