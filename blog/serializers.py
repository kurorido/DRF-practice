from rest_framework import serializers
from blog.models import Article, Tag
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('username',)  

class ArticleSerializer(serializers.ModelSerializer):
	
	tags = serializers.RelatedField(many=True)
	author = serializers.RelatedField()

	class Meta:
		model = Article
		fields = ('title','author','content','tags')
		
	owner = serializers.Field(source='owner.username')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('tag_name',)